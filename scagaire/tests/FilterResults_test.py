import unittest
import os
import shutil
from scagaire.FilterResults  import FilterResults

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','filter_results')

class TestFilterResults(unittest.TestCase):
    
    def test_metagenomic_results_abricate(self):
        f =  FilterResults(os.path.join(data_dir, 'metagenomic_results.abricate'), os.path.join(data_dir, 'database'), 0, None, 'resfinder',False)
        
        self.assertEqual(len(f.filter_by_species('Escherichia coli')), 18)
        self.assertEqual(len(f.filter_by_species('Clostridioides difficile')), 65)
        
    def test_metagenomic_results_staramr(self):
        f =  FilterResults(os.path.join(data_dir, 'metagenomics_results.staramr'), os.path.join(data_dir, 'database'), 0, None, 'resfinder', False)
        
        self.assertEqual(len(f.filter_by_species('Escherichia coli')), 4)
        self.assertEqual(len(f.filter_by_species('Clostridioides difficile')), 13)