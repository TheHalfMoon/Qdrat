# Build stage - for compiling dependencies
#
# The base is pinned by manifest digest, not by tag. `python:3.12-slim` is a
# moving target: the same Dockerfile could build a different image next month
# and nothing in the build would say so. The digest below is exactly the image
# G0-01 resolved the linux-amd64 CPython 3.12 lock against, so the interpreter
# that installs the lock is the interpreter the lock was frozen for. Changing it
# means re-freezing the lock, which is why docker/image-digests.json records
# where this digest came from.
FROM python:3.12-slim@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install build dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
        libcairo2-dev \
        libpango1.0-dev \
        libgdk-pixbuf-xlib-2.0-dev \
        libxml2-dev \
        libxslt1-dev \
        libffi-dev \
        pkg-config \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install the frozen dependency set.
#
# The image installs from requirements/locks/linux-amd64-py312.txt - the same
# 149 pinned, hash-carrying distributions G0-01 proved installable offline - and
# not from requirements.txt, whose ranges let pip resolve something different on
# every build. docker/lock-requirements.py renders the one locked artifact that
# is not published on an index (en_core_web_sm, a GitHub release asset) as
# `name @ url#sha256=...`, taking the URL from the artifact inventory, so the
# whole set installs in one hash-checked pass. Nothing here runs
# `pip install --upgrade pip`: the interpreter that resolves the lock is the
# digest-pinned base image's own pip, and upgrading it would reintroduce an
# unpinned resolver into a build whose point is that nothing is unpinned.
COPY requirements/locks/linux-amd64-py312.txt requirements/locks/
COPY requirements/artifacts/linux-amd64-py312.json requirements/artifacts/
COPY docker/lock-requirements.py docker/
RUN python docker/lock-requirements.py \
        --lock requirements/locks/linux-amd64-py312.txt \
        --artifacts requirements/artifacts/linux-amd64-py312.json \
        --out /tmp/requirements.lock.txt \
    && python -m pip install --no-cache-dir --require-hashes \
        -r /tmp/requirements.lock.txt \
    && rm -f /tmp/requirements.lock.txt

# Production stage - minimal runtime image
FROM python:3.12-slim@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Install only runtime dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
        libjpeg62-turbo \
        zlib1g \
        libcairo2 \
        libpango-1.0-0 \
        libgdk-pixbuf-xlib-2.0-0 \
        libxml2 \
        libxslt1.1 \
        libffi8 \
        curl \
        netcat-openbsd \
        gettext \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# The base image ships its own setuptools (and pip's vendored msgpack) in
# /usr/local/lib/python3.12/site-packages, outside the /opt/venv this app
# runs from. Pinning them in requirements.txt only fixes the venv copy, so
# the image scan kept failing on the system copy: setuptools 70.3.0
# (CVE-2025-47273, path traversal) and msgpack 1.1.2
# (GHSA-6v7p-g79w-8964, out-of-bounds read). Nothing in the app imports
# them from there, but they are in the image, so they are the image's
# problem.
# /usr/local/bin/python explicitly: ENV PATH above already points at
# /opt/venv/bin, which does not exist yet at this layer.
RUN /usr/local/bin/python -m pip install --no-cache-dir --upgrade \
        "setuptools>=78.1.1" "msgpack>=1.2.1"

# Create non-root user FIRST
RUN useradd --create-home --uid 1000 appuser

# Copy virtual environment from builder stage WITH correct ownership
COPY --from=builder --chown=appuser:appuser /opt/venv /opt/venv

WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Compile gettext catalogs (.po -> .mo): nothing in the repo or the runtime
# compiles them, so without this every non-English locale silently renders
# English. Plain msgfmt, so no Django settings/DB are needed at build time.
RUN find . -name '*.po' -execdir sh -c 'msgfmt "$1" -o "${1%.po}.mo"' _ {} \;

# Copy entrypoint script
COPY --chown=appuser:appuser docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Both COPYs above already set --chown, so only the new dirs need ownership;
# a recursive chown over /app would duplicate a whole layer for no gain.
RUN mkdir -p staticfiles media \
    && chown appuser:appuser staticfiles media

USER appuser

# Build metadata. VERSION should match horilla/__version__.py and the release
# tag; the publish workflow passes all three and fails if they disagree.
ARG VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown
LABEL org.opencontainers.image.title="Horilla HR" \
      org.opencontainers.image.description="Free and open source HR software" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.source="https://github.com/horilla/horilla-hr" \
      org.opencontainers.image.url="https://www.horilla.com" \
      org.opencontainers.image.documentation="https://docs.horilla.com" \
      org.opencontainers.image.vendor="Horilla" \
      org.opencontainers.image.licenses="LGPL-2.1"

# The same build identity, as environment variables the entrypoint logs at
# startup. A container cannot read its own image digest from inside, and a log
# line that only says "Starting Horilla HR..." cannot be tied to the image that
# produced it. With these, the startup banner names the revision and build date
# baked into the image, so docker/image-digests.json can bind a captured log to
# the exact image digest it came from.
ENV QDRAT_BUILD_VERSION="${VERSION}" \
    QDRAT_BUILD_REVISION="${VCS_REF}" \
    QDRAT_BUILD_DATE="${BUILD_DATE}"

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "horilla.wsgi:application", "--config", "docker/gunicorn.conf.py"]
