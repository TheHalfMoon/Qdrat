"""Read-only structural validation of the canonical plan; no product-test claims."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC_SHA = '5de7d6499bb0a9e3a191fc0934399cf099d1980a'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def ordered(rows, label):
    by_id = {row['id']: row for row in rows}
    require(len(by_id) == len(rows), f'{label}: duplicate IDs')
    seen, active, result = set(), set(), []
    def visit(key):
        require(key in by_id, f'{label}: missing dependency {key}')
        require(key not in active, f'{label}: cycle at {key}')
        if key in seen:
            return
        active.add(key)
        deps = by_id[key]['dependencies']
        require(len(set(deps)) == len(deps), f'{label}: duplicate edge {key}')
        for dep in deps:
            visit(dep)
        active.remove(key)
        seen.add(key)
        result.append(key)
    for key in sorted(by_id):
        visit(key)
    return result

def content_manifest():
    # Proof outputs and the transport seal cannot hash themselves. Inputs and
    # review narrative are included; excluded files are named explicitly.
    files = {}
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT).as_posix()
        if (not path.is_file() or '__pycache__' in path.parts or
                rel.startswith('evidence/verification/') or rel == 'evidence/transport-seal.json'):
            continue
        files[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    digest = hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',', ':')).encode()).hexdigest()
    return {'sha256': digest, 'files': files,
            'excluded': ['evidence/verification/**', 'evidence/transport-seal.json', '**/__pycache__/**']}

def validate(specgrain_source=None):
    for number in range(44):
        matches = list(ROOT.glob(f'{number:02d}_*.md'))
        require(len(matches) == 1, f'missing/duplicate canonical chapter {number:02d}')
    for name in ('README.md','CONTRACTS.md','DOMAIN_SCHEMAS.md','REVIEW_LOG.md','plan-policy.toml'):
        require((ROOT/name).is_file(), f'missing {name}')
    graph, tasks, nodes = read('EXECUTION_GRAPH.yaml'), read('tasks/tasks.json'), read('specgrain/nodes.json')
    require(graph['schema'] == 'qdrat.execution-graph/v1', 'unknown graph schema')
    task_order, gate_order = ordered(graph['tasks'],'task graph'), ordered(graph['gates'],'gate graph')
    ordered(nodes,'SpecNode dependency graph')
    tmap, nmap = {t['id']:t for t in tasks}, {n['id']:n for n in nodes}
    gates = {g['id']:g for g in graph['gates']}
    require(len(tmap) == len(tasks) == len(nodes) == 96, 'task/node cardinality or duplicates')
    require(set(tmap) == set(task_order), 'graph/record mismatch')
    require(len(gates) == 13, 'gate count')
    require(graph['first_task'] == 'G0-01' and not tmap['G0-01']['dependencies'], 'first frontier')
    require(graph['current_gate'] == 'G0', 'unexpected claimed gate advancement')
    required = ('objective','problem','current_state_evidence','scope','expected_repository_areas',
        'interfaces','schema_changes','source_inputs','security_privacy_requirements',
        'migration_requirements','ux_requirements','implementation_guidance','non_goals',
        'forbidden_shortcuts','acceptance','tests','evidence_required','rollback','completion_state',
        'next_authorized_state','contract_ids')
    contracts = (ROOT/'CONTRACTS.md').read_text(encoding='utf-8')
    listed = []
    for g in gates.values():
        listed.extend(g['tasks'])
        require(len(g['exit']) >= 3, f'{g["id"]}: measurable exits absent')
        require(all(tmap[t]['gate'] == g['id'] for t in g['tasks']), f'{g["id"]}: task ownership')
        needed = {gates[d]['tasks'][-1] for d in g['dependencies']}
        require(needed <= set(tmap[g['tasks'][0]]['dependencies']), f'{g["id"]}: gate predecessor edge missing')
    require(len(listed) == len(set(listed)) and set(listed) == set(tmap), 'gate task partition')
    for ref in graph['tasks']:
        t=tmap[ref['id']]; n=nmap[t['grain_id']]
        require(all(t.get(k) for k in required), f'{t["id"]}: incomplete record')
        require(ref['dependencies'] == t['dependencies'], f'{t["id"]}: graph dependencies drift')
        require(n['dependencies'] == [tmap[d]['grain_id'] for d in t['dependencies']], f'{t["id"]}: node edges drift')
        require(n['acceptance'] == t['acceptance'] and n['outcome'] == t['objective'], f'{t["id"]}: spec drift')
        require(n['state'] == t['state'] == ref['state'], f'{t["id"]}: state drift')
        require(t['state'] in ('SHAPED','REFINING'), f'{t["id"]}: fabricated implementation state')
        for c in t['contract_ids']:
            require(re.search(r'^## '+re.escape(c)+r'\b', contracts, re.M), f'{t["id"]}: missing {c}')
        for path in t['plan_inputs']+t['source_inputs']:
            require((ROOT/path).is_file(), f'{t["id"]}: missing input {path}')
        actual_downstream={x['id'] for x in tasks if t['id'] in x['dependencies']}
        require(actual_downstream == set(t['downstream_unlocks']), f'{t["id"]}: downstream edges drift')
    inventories = [('founder-inventory.json','repositories',36),('authorized-sources.json','sources',76),('discovered-sources.json','sources',36)]
    for filename,key,count in inventories:
        items=read('evidence/'+filename)[key]
        require(len(items) == count, filename+': count')
        require(len({x['repository'].lower() for x in items}) == count, filename+': duplicates')
        require(all(x['classification'] in ('COPY_COMPONENT','ADAPT_PATTERN','RUN_AS_SERVICE','DEPENDENCY','REFERENCE_ONLY','REJECT') for x in items), filename+': classification')
        for item in items:
            if item.get('head'):
                require(re.fullmatch('[0-9a-f]{40}',item['head']),filename+': nonimmutable revision')
    require(sum(x['visibility']=='private' for x in read('evidence/founder-inventory.json')['repositories']) == 7, 'private count')
    # Validate relative links in canonical prose, avoiding URL fragments/remote schemes.
    for path in ROOT.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            target=target.split('#')[0]
            require((path.parent/target).exists(),f'{path.name}: broken local link {target}')
    result={'schema':'qdrat.plan-validation/v1','status':'PASS','product_tests':'NOT_RUN',
            'tasks':len(tasks),'nodes':len(nodes),'gates':len(gates),'task_order':task_order,'gate_order':gate_order,
            'content_manifest':content_manifest(),'specgrain':{'status':'NOT_RUN'}}
    if specgrain_source:
        source=Path(specgrain_source).resolve()
        sha=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
        require(sha == SPEC_SHA,'SpecGrain source SHA mismatch')
        dirty=subprocess.check_output(['git','-C',str(source),'status','--porcelain'],text=True).strip()
        require(not dirty,'SpecGrain source has modifications')
        sys.dont_write_bytecode=True
        sys.path.insert(0,str(source/'src'))
        from specgrain.model import SpecNode
        from specgrain.refinement import validate_refinement
        from specgrain.readiness import evaluate_grain_readiness
        forest=[SpecNode.from_dict(n) for n in nodes]
        validate_refinement(forest)
        first=next(n for n in forest if n.id=='SG-000001')
        readiness=evaluate_grain_readiness(first,forest)
        require(readiness.is_ready,'SpecGrain readiness: '+str(readiness.issues))
        result['specgrain']={'status':'PASS','source_sha':sha,'parsed_nodes':len(forest),
            'refinement_forest':'PASS','candidate_id':first.id,'revision_digest':readiness.revision_digest,
            'is_ready':readiness.is_ready,'issues':[],'implementation_verified':False}
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--specgrain-source')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        result=validate(args.specgrain_source)
    except (ValueError,KeyError,OSError,ImportError,subprocess.SubprocessError) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)}))
        return 1
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('content_manifest','task_order','gate_order')}))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
