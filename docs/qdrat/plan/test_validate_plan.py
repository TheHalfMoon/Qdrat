"""Adversarial checks for graph/evidence validation, using disposable plan copies."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

source=Path(__file__).with_name('validate_plan.py')
spec=importlib.util.spec_from_file_location('qdrat_plan_validator',source)
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class PlanValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.original=validator.ROOT
        validator.ROOT=Path(self.temp.name)/'plan'
        shutil.copytree(self.original,validator.ROOT,ignore=shutil.ignore_patterns('__pycache__','verification'))

    def tearDown(self):
        validator.ROOT=self.original
        self.temp.cleanup()

    def change(self,path,mutate):
        target=validator.ROOT/path
        obj=json.loads(target.read_text(encoding='utf-8'))
        mutate(obj)
        target.write_text(json.dumps(obj),encoding='utf-8')

    def test_valid_plan(self):
        self.assertEqual(validator.validate()['status'],'PASS')

    def test_cycle_rejected(self):
        self.change('EXECUTION_GRAPH.yaml',lambda g:g['tasks'][0]['dependencies'].append('G0-02'))
        with self.assertRaisesRegex(ValueError,'cycle'):
            validator.validate()

    def test_acceptance_drift_rejected(self):
        self.change('specgrain/nodes.json',lambda n:n[0]['acceptance'].append('silently weakened alternate acceptance'))
        with self.assertRaisesRegex(ValueError,'spec drift'):
            validator.validate()

    def test_missing_gate_predecessor_rejected(self):
        self.change('tasks/tasks.json',lambda ts:next(t for t in ts if t['id']=='G9-01')['dependencies'].remove('G6-08'))
        with self.assertRaisesRegex(ValueError,'gate predecessor edge'):
            validator.validate()

    def test_unclassified_source_rejected(self):
        self.change('evidence/authorized-sources.json',lambda s:s['sources'][0].update(classification='AUTO_APPROVED'))
        with self.assertRaisesRegex(ValueError,'classification'):
            validator.validate()

    def test_false_completion_rejected(self):
        self.change('tasks/tasks.json',lambda t:t[0].update(state='VERIFIED'))
        self.change('specgrain/nodes.json',lambda n:n[0].update(state='VERIFIED'))
        self.change('EXECUTION_GRAPH.yaml',lambda g:g['tasks'][0].update(state='VERIFIED'))
        with self.assertRaisesRegex(ValueError,'fabricated implementation state'):
            validator.validate()

    def test_missing_contract_rejected(self):
        self.change('tasks/tasks.json',lambda t:t[0]['contract_ids'].append('C99'))
        with self.assertRaisesRegex(ValueError,'missing C99'):
            validator.validate()

if __name__=='__main__':
    unittest.main()
