import unittest
import os
import shutil
from scagaire.parser.Staramr  import Staramr

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','parser','staramr')

class TestStaramr(unittest.TestCase):
    
    def test_header_only(self):
        a = Staramr(os.path.join(data_dir, 'header_only.staramr'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(a.results, [])
        
    def test_metagenomic_results(self):
        a = Staramr(os.path.join(data_dir, 'metagenomics_results.staramr'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(len(a.results), 26)
        