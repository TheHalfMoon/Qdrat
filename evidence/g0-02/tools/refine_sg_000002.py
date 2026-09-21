"""Refine SG-000002 against the accepted predecessor and emit its execution records.

This is the real SpecGrain library at the pinned revision, not a prose emulation:
the refined node is parsed by ``SpecNode.from_dict``, the whole forest is checked
by ``validate_refinement``, readiness is decided by ``evaluate_grain_readiness``,
and the WorkPacket is built by ``build_work_packet`` from revision-bound context
sources with a deterministic context budget.

Run from the repository root:

    python evidence/g0-02/tools/refine_sg_000002.py \
        --specgrain-source <checkout of 5de7d6499bb0a9e3a191fc0934399cf099d1980a>

It writes three records next to the repository's other machine evidence:
``refinement.json``, ``specgrain-readiness.json`` and ``workpacket.json``.
Nothing here claims the implementation succeeded; readiness is a specification
state, not a test result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
NODES_PATH = REPO_ROOT / "docs" / "qdrat" / "plan" / "specgrain" / "nodes.json"
OUT_DIR = REPO_ROOT / "evidence" / "g0-02"
SPEC_ID = "SG-000002"
PREDECESSOR_ID = "SG-000001"
PREDECESSOR_REVISION = "ca5ceb361798ff8ba78a8ac86c47de0bc440058e"
PREDECESSOR_ACCEPTED_HEAD = "b4531988f4a32143407c5aa2de4d7090d33e4930"
PREDECESSOR_RECEIPT_COMMIT = "2d4abc05c4a80e5d9b7a629bac52ed021d8279bb"

# Context sourcing: the exact files this grain has to bind, read at the accepted
# predecessor, with the byte count that is actually on disk and a token cost
# derived from it. Sizes are measured, not guessed, so the budget report below
# can be re-derived by anyone who checks out that revision.
# (source_id, path, selection reason, requirement)
CONTEXT_FILES = [
    ("dockerfile", "Dockerfile", "The image build this grain must make reproducible.", "required"),
    (
        "compose-dev",
        "docker-compose.yml",
        "Development stack whose image references and bootstrap order this grain pins.",
        "required",
    ),
    (
        "compose-prod",
        "docker-compose.prod.yml",
        "Production overlay; carries the other half of the image references.",
        "required",
    ),
    (
        "entrypoint",
        "docker/entrypoint.sh",
        "Release tasks (migrate, collectstatic) and their ordering under container start.",
        "required",
    ),
    (
        "lock",
        "requirements/locks/linux-amd64-py312.txt",
        "The frozen artifact set this image must install from instead of requirements.txt.",
        "required",
    ),
    (
        "inventory",
        "requirements/artifacts/linux-amd64-py312.json",
        "Artifact inventory binding every distribution to its URL, hash and licence.",
        # Read at the frontier to bind the URL and hash of the one direct
        # artifact, but 167 KB of JSON is not worth loading as context: the lock
        # file already carries the pinned set, and the inventory is bound by
        # digest in the packet decisions. Kept optional and priority-last so the
        # budget omits it rather than truncating a required source.
        "optional",
    ),
    (
        "supply-chain-plan",
        "docs/qdrat/plan/35_SUPPLY_CHAIN_PROVENANCE_PLAN.md",
        "Normative provenance obligations for image digests and OS package inventory.",
        "required",
    ),
    (
        "gate-plan",
        "docs/qdrat/plan/39_GATE_PLAN.md",
        "The G0 exit this grain contributes to, including the CI obligation.",
        "required",
    ),
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def token_cost(size_bytes: int) -> int:
    return max(1, size_bytes // 4)


def context_sources(ContextSource):
    sources = []
    for source_id, relative, reason, requirement in CONTEXT_FILES:
        path = REPO_ROOT / relative
        size = path.stat().st_size
        sources.append(
            ContextSource(
                source_id=source_id,
                provenance=f"repo:{relative}",
                selection_reason=reason,
                revision=f"git:{PREDECESSOR_ACCEPTED_HEAD}",
                size_bytes=size,
                token_cost=token_cost(size),
                requirement=requirement,
                priority=1 if requirement == "optional" else 0,
            )
        )
    return sources


def refined_node(frozen: dict) -> dict:
    node = dict(frozen)
    node["state"] = "REFINING"
    # Measured context, not the planning estimate: the frozen node carried
    # budget_tokens 16000 / estimated_tokens 12000 from the plan, and the eight
    # sources this grain actually reads at the frontier total 212 KB, of which
    # 45 KB is required. The budget below covers the required sources with room
    # for one more; the 167 KB artifact inventory is declared optional above and
    # is therefore omitted rather than allowed to evict a required source.
    node["context"] = {"budget_tokens": 20000, "estimated_tokens": 13000}
    metadata = dict(node.get("metadata", {}))
    metadata["task_id"] = "G0-02"
    metadata["task_record"] = "tasks/tasks.json"
    metadata["contracts"] = ["C10"]
    metadata["readiness"] = {
        "version": 1,
        # The frozen decision is resolved, not dropped: it is recorded below.
        "unresolved_decisions": [],
        "minimality": {
            "choice": "reuse-existing",
            "rationale": (
                "The image, both compose files and the entrypoint already exist and are "
                "qualified by the inherited baseline. This grain changes what the build "
                "installs (the frozen lock from SG-000001 instead of requirements.txt) and "
                "pins the images it names; it introduces no new service, no new dependency "
                "and no new runtime component."
            ),
        },
        "safety": {
            "status": "requirements-defined",
            "requirements": [
                "The build installs only hash-verified artifacts from the frozen inventory; no index-resolved or unhashed package reaches the image.",
                "No secret, credential or production personal data is written into an image layer, a compose file or an evidence record; compose interpolation secrets are supplied through a temporary env file outside the repository.",
                "Every image reference in the Dockerfile and both compose files is pinned to a resolved manifest digest, so a rebuild cannot silently pick up a different base or service image.",
            ],
        },
    }
    metadata["execution_refinement"] = {
        "predecessor": {
            "grain": PREDECESSOR_ID,
            "implementation_revision": PREDECESSOR_REVISION,
            "accepted_head": PREDECESSOR_ACCEPTED_HEAD,
            "acceptance_receipt_commit": PREDECESSOR_RECEIPT_COMMIT,
        },
        "decisions_resolved": [
            {
                "frozen_decision": "Execution packet must bind current implementation paths, exact commands and predecessor evidence at the frontier; accepted architecture may not be changed implicitly.",
                "resolution": "Paths bound at the accepted head: Dockerfile, docker/, docker-compose.yml, docker-compose.prod.yml plus the repository-level Diffcipline policy that currently forbids the Dockerfile; commands bound in evidence/g0-02/workpacket.json; predecessor evidence bound by the acceptance receipt commit named above.",
            },
            {
                "decision": "The image installs from requirements/locks/linux-amd64-py312.txt, generated for linux/amd64 CPython 3.12, rather than from requirements.txt.",
                "reason": "G0-01 froze that target for exactly this base image family and explicitly deferred wiring it into the build to this grain.",
            },
            {
                "decision": "The direct-URL spaCy model stays a single direct artifact: the build composes it into a generated requirements file as name @ url#sha256, taken from the artifact inventory rather than repeated in the Dockerfile.",
                "reason": "One source of truth for the URL and hash; pip verifies it under --require-hashes.",
            },
        ],
        "scope_note": "The task's change surface ('Dockerfile', 'docker/', 'docker-compose.yml', 'docker-compose.prod.yml') is preserved. Two bounded additions are required to make that surface provable and are recorded rather than assumed: the repository-level Diffcipline policy must stop forbidding the Dockerfile in an explicit reviewed commit, and the task publishes its own bounded policy.",
    }
    node["metadata"] = metadata
    return node


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--specgrain-source", required=True)
    args = parser.parse_args()

    source = Path(args.specgrain_source).resolve()
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(source / "src"))

    from specgrain.context import ContextBudgetPolicy, evaluate_context_budget
    from specgrain.model import SpecNode
    from specgrain.packet import build_work_packet
    from specgrain.readiness import evaluate_grain_readiness
    from specgrain.refinement import validate_refinement

    frozen_nodes = json.loads(NODES_PATH.read_text(encoding="utf-8"))
    by_id = {node["id"]: node for node in frozen_nodes}
    refined = refined_node(by_id[SPEC_ID])

    forest_data = [
        refined if node["id"] == SPEC_ID else node for node in frozen_nodes
    ]
    forest = [SpecNode.from_dict(node) for node in forest_data]
    issues = validate_refinement(forest)
    if issues:
        raise SystemExit(f"refinement forest invalid: {issues}")

    candidate = next(node for node in forest if node.id == SPEC_ID)
    parent = next(node for node in forest if node.id == PREDECESSOR_ID)
    readiness = evaluate_grain_readiness(candidate, forest)
    if not readiness.is_ready:
        raise SystemExit(
            "grain readiness failed: "
            + "; ".join(f"{issue.code.value}: {issue.message}" for issue in readiness.issues)
        )

    from specgrain.context import ContextSource

    sources = context_sources(ContextSource)
    policy = ContextBudgetPolicy(
        max_tokens=int(candidate.context["budget_tokens"]),
        max_bytes=None,
        max_sources=None,
    )
    report = evaluate_context_budget(sources, policy)
    if not report.fits:
        raise SystemExit(f"context budget failed: {report.to_dict()}")

    packet = build_work_packet(
        candidate,
        [source for source in sources if source.source_id in report.selected_ids],
        report,
        decisions=[
            f"Predecessor: {PREDECESSOR_ID} at {PREDECESSOR_REVISION}, accepted head {PREDECESSOR_ACCEPTED_HEAD}, receipts sealed at {PREDECESSOR_RECEIPT_COMMIT}.",
            "Install the frozen lock into the image with --require-hashes; the direct spaCy artifact is expressed as name @ url#sha256 taken from the artifact inventory.",
            "Pin every image reference (Dockerfile stages, postgres, redis, nginx) to a resolved manifest digest.",
            "Record the OS package inventory of the built image inside the image and in evidence.",
            "Serialise the release tasks so two containers starting together cannot run migrations concurrently.",
        ],
        assumptions=[
            "The accepted head's frozen lock still describes requirements.txt; the lock is frozen and this grain must not change it.",
            "Docker on the development host can reach the registry and the package index for the build; the install proof itself is hash-verified.",
            "The image is built and run on linux/amd64, the only platform G0-01 qualified.",
        ],
        minimality_evidence=[
            "No new runtime dependency, service or component is added to the stack.",
            "The base image digest chosen for the Dockerfile is the same digest G0-01 resolved and froze against.",
            "Existing entrypoint structure, compose service graph and healthchecks are preserved; only digests, the install source and the release-task serialisation change.",
        ],
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "refinement.json").write_text(
        json.dumps(
            {
                "schema": "qdrat.specgrain-refinement/v1",
                "spec_id": SPEC_ID,
                "task_id": "G0-02",
                "state_before": by_id[SPEC_ID]["state"],
                "state_after": candidate.state,
                "parent": PREDECESSOR_ID,
                "predecessor": {
                    "implementation_revision": PREDECESSOR_REVISION,
                    "accepted_head": PREDECESSOR_ACCEPTED_HEAD,
                    "acceptance_receipt_commit": PREDECESSOR_RECEIPT_COMMIT,
                    "parent_revision_digest": parent.revision_digest,
                },
                "frozen_revision_digest": SpecNode.from_dict(by_id[SPEC_ID]).revision_digest,
                "refined_revision_digest": candidate.revision_digest,
                "acceptance_preserved": list(candidate.acceptance),
                "acceptance_unchanged_from_frozen": list(candidate.acceptance)
                == list(SpecNode.from_dict(by_id[SPEC_ID]).acceptance),
                "scope_in_unchanged_from_frozen": list(candidate.scope_in)
                == list(SpecNode.from_dict(by_id[SPEC_ID]).scope_in),
                "refined_node": candidate.to_dict(),
                "children": [],
                "split_rationale": (
                    "The grain stays one leaf: it is a single vertical slice over one "
                    "deployment surface, and its five acceptance criteria are proved by one "
                    "build, one compose validation, one migration run on an empty database, a "
                    "repeated bootstrap and a digest binding. Nothing in it can be proved "
                    "independently of the others."
                ),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (OUT_DIR / "specgrain-readiness.json").write_text(
        json.dumps(
            {
                "schema": "qdrat.grain-readiness/v1",
                "spec_id": SPEC_ID,
                "candidate_revision_digest": readiness.revision_digest,
                "is_ready": readiness.is_ready,
                "issues": [
                    {"code": issue.code.value, "field": issue.field, "message": issue.message}
                    for issue in readiness.issues
                ],
                "context_budget": report.to_dict(),
                "forest_size": len(forest),
                "implementation_verified": False,
                "note": "Grain readiness is a specification state: it says the grain is bounded and executable, not that it passed.",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (OUT_DIR / "workpacket.json").write_text(
        json.dumps(
            {
                "specgrain_source_sha": "5de7d6499bb0a9e3a191fc0934399cf099d1980a",
                "spec_revision_digest": candidate.revision_digest,
                "context_plan_digest": report.plan_digest,
                "base_revision": PREDECESSOR_ACCEPTED_HEAD,
                "workpacket": packet.to_dict(),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "spec_id": SPEC_ID,
                "is_ready": readiness.is_ready,
                "revision_digest": readiness.revision_digest,
                "packet_digest": packet.packet_digest,
                "context_plan_digest": report.plan_digest,
                "context_tokens": report.selected_tokens,
                "context_budget": policy.max_tokens,
                "context_sources": len(report.selected_ids),
                "written": [str(path) for path in sorted(OUT_DIR.glob("*.json"))],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
