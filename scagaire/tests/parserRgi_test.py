import unittest
import os
import shutil
from scagaire.parser.Rgi  import Rgi

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','parser','rgi')

class TestRgi(unittest.TestCase):
    
    def test_header_only(self):
        a = Rgi(os.path.join(data_dir, 'header_only.rgi'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(a.results, [])
        
    def test_metagenomic_results(self):
        a = Rgi(os.path.join(data_dir, 'metagenomic_results.rgi'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(len(a.results), 5)
        
        self.assertEqual(sorted([r.gene for r in a.results]), ["APH(3'')-Ib", "APH(3'')-Ib", 'APH(6)-Id', 'sul2', 'sul2']) 
        