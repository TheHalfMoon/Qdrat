# Master execution plan

The machine records in tasks/tasks.json are the complete task packets at planning resolution: objective, current-state evidence, exact scope, expected areas, interfaces/schema/API constraints, sources, privacy/security, migration, UX, implementation guidance, non-goals, acceptance/tests, evidence, rollback and downstream authorization. Physical paths and commands are reconciled at each future head before GRAIN readiness; this prevents false precision about files not created yet.

Current frontier: G0-01 / SG-000001. Do not start new product implementation before baseline gates. The source inputs and target contracts are fixed; future refinement may split a task into dependency-preserving child grains but may not invent another identity, engine or authority.

| Gate | Depends on | Task range | Result |
|---|---|---|---|
| G0 | Live truth | G0-01 … G0-06 | Baseline |
| G1 | G0 | G1-01 … G1-11 | Kernel and trust |
| G2 | G1 | G2-01 … G2-08 | Data connections |
| G3 | G1 | G3-01 … G3-08 | Durable automation |
| G4 | G2, G3 | G4-01 … G4-12 | People core and knowledge |
| G5 | G4 | G5-01 … G5-06 | Saudi payroll qualification |
| G6 | G4 | G6-01 … G6-08 | Work and Service |
| G7 | G6 | G7-01 … G7-10 | Commercial and asset operations |
| G8 | G4 | G8-01 … G8-07 | Studio analytics and extensions |
| G9 | G4, G6 | G9-01 … G9-09 | AI execution and voice |
| G10 | G5 | G10-01 … G10-06 | Production operations and release |
| G11 | G10 | G11-01 … G11-03 | HA and scale |
| G12 | G7, G9, G11 | G12-01 … G12-02 | Later domain replacement admission |

## Bounded execution rule

One implementation turn selects one leaf grain and its work packet. Target one owned contract change and one independently provable outcome. If context exceeds 16,000 estimated tokens, unrelated domain lifecycles would change together, or acceptance cannot be proved in a reviewable diff, split before implementation: schema/invariants → command/query → UI/adapter → recovery/qualification. Preserve parent acceptance as the union of children, add dependency edges and validate the graph. This is ordinary SpecGrain refinement, not authorization to defer the parent outcome or replace architecture with a vague epic.

G4-11 (learning/skills/scenarios), G6-07 (catalog/incident/problem/change), G7-10 (CI/facilities), G8-03 (formulas/views) and G9-09 (desktop/meetings) are intentionally SHAPED work packages. Their first implementation action is this bounded refinement; they are not represented as immediately executable one-diff grains. Their domain contracts and required acceptance are already specified. G12 nodes produce admission specifications, not unrestricted implementation authority.

The 96 task definitions are executable only through this readiness procedure; exactly one is the initial dependency-free readiness candidate. Implementation evidence remains future work.
