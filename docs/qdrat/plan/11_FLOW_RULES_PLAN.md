# Flow and Rules

Owner: qdrat/automation. WorkflowRevision is an immutable typed graph with input/output schemas, node IDs, declared dependencies, source revisions and publication policy. Initial nodes: action, condition, bounded foreach, parallel join, wait-until, wait-signal, approval, subflow and return. Agent/sandbox nodes call typed actions after their gates.

Graph validation rejects unknown nodes, unreachable outputs, incompatible edges, cycles outside bounded foreach, unbounded recursion, missing timeout/cancellation policy and undeclared side effects. A published revision is immutable; edits create a new revision. Running instances keep their original revision. Migration of live runs is a separate reviewed operation with a before/after state mapping; default is finish old revision.

Rules are pure functions from typed input plus explicit evaluation_time to typed result and trace. Initial expression AST supports literal, field, comparison, boolean conjunction, conditional, membership, bounded collection aggregate and fixed-decimal arithmetic. Null, missing, denied and unknown are distinct. No eval, Python, arbitrary JS, filesystem, network or implicit clock. Bound depth, collection size and instruction count. Division/overflow/type errors produce typed failures, never silent zero.

Decision tables define first-match or collect semantics explicitly, ordering, overlap detection, default result and test vectors. GoRules/zen and CEL are references; evaluate a pinned engine only if compatibility with decimal, unknown, resource-bound and offline semantics is proved. Business routing cannot override Trust decisions. Payroll country calculations use versioned typed rules with separately qualified rounding and legal effective dates, not generic editor freedom.

Preview uses fixture/snapshotted inputs and mock actions; it cannot send mail or mutate a source. Simulation produces a diff of intended effects, policy decisions and estimated cost. Publishing requires author/reviewer segregation for R3 policies. Replay is deterministic over recorded inputs; nondeterministic model outputs remain recorded observations, not recomputed truth.

Acceptance: reject cyclic/ill-typed plans, stable output across restart, no duplicate external effect after lease loss, expiry/revocation during approval wait, deterministic DST schedule behavior and bounded fan-out under cancellation. Usability evidence must show a nontechnical admin can edit a leave-routing rule without changing permission semantics.
