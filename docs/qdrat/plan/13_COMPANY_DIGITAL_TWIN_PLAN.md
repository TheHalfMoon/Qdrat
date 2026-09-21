# Company Digital Twin

Owner: qdrat/kernel for ObjectRef; qdrat/data for sourced observations; qdrat/knowledge for derived graph querying. Domain modules own their entities and authoritative relationships. The twin is a semantic view, not a graph database that can overwrite payroll or identity.

Relationship = tenant, relation_type, subject_ref, object_ref, valid_from/to, recorded_at, source_id/revision, evidence_ref, confidence, authority_owner, classification and deletion state. A typed relation catalog declares endpoint types, cardinality, temporal constraints and permitted inference. Observed “runs_on” differs from approved “owned_by”. An LLM-inferred edge is a proposal/observation until reviewed where policy requires.

Initial PostgreSQL adjacency projection supports bounded traversals. Queries carry depth, node/edge and time budgets plus C07 policy. Every endpoint and edge must be visible; hiding a node while returning its identifying edge/count is forbidden. Bulk graph export is a separate permission. No Neo4j/Memgraph dependency in the default profile.

Projection consumption is idempotent and checkpointed. Rebuild into a shadow generation, compare invariants and atomically switch a generation pointer. Preserve tombstones and revocations during rebuild. Graph failure leaves transactional APIs usable.

Initial journeys: person → employment → manager → assigned assets; service → owner → incidents → related work; opportunity → contract → service case → invoice reference. Later skill/capacity graphs support planning without automatic employment decisions.

Graphify and code-graph-rag supply extraction/explanation ideas; company authority does not derive from their code-analysis schemas. Provenance and confidence must appear in “why linked?” UI. Health measures projection lag, orphan references, conflicting authority and stale observations. Tests prove date boundaries, restricted nodes, source deletion and rebuild equivalence.
