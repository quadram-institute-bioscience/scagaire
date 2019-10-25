import unittest
import os
import shutil
from scagaire.parser.Abricate097  import Abricate097

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','parser','abricate097')

class TestAbricate097(unittest.TestCase):
    
    def test_header_only(self):
        a = Abricate097(os.path.join(data_dir, 'header_only.abricate'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(a.results, [])
           
    def test_metagenomic_results(self):
        a = Abricate097(os.path.join(data_dir, 'metagenomic_results.abricate'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(len(a.results), 4)
