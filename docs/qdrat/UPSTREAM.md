# Qdrat People — Horilla Upstream Policy

## Imported baseline

Qdrat `main` was initialized from the Horilla `2.0` branch at commit:

`e2d288940aab52af881786678b2fc86dfa5c272a`

The Git history was preserved rather than copying files into a new root commit. The local canonical checkout also keeps a `horilla-upstream` remote pointing at the public Horilla repository.

## Sync policy

Horilla updates are never merged blindly. Upstream updates enter a dedicated synchronization branch, are reviewed as a diff from the last accepted upstream commit, and pass Qdrat tests, schema/migration review, license/provenance checks, and security gates before merge.

Qdrat-owned domain changes should minimize invasive edits to inherited modules until replacement boundaries are established. New architecture should prefer adapters and Qdrat-owned modules so upstream fixes remain reviewable.

## Branding and attribution

Qdrat will develop its own product identity and UI while retaining required LGPL notices, copyright notices, license text, and source/modification obligations applicable to inherited Horilla code. Modified inherited code should remain identifiable through Git history and normal repository provenance.
