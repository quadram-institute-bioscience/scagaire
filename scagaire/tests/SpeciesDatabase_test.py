import unittest
import os
import shutil
import filecmp
from scagaire.SpeciesDatabase import SpeciesDatabase

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','species_database')

class TestSpeciesDatabase(unittest.TestCase):
    
    def test_header_only(self):
        s = SpeciesDatabase('outputfile', 'genus species', 'ncbi', fixed_time = '20101010')
        s.output_genes_to_freq_file({'abc': 5, 'efg':10, 'zzz123':1})
        self.assertTrue(os.path.exists('outputfile'))
        
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_output_file"), "outputfile")
        )
        
        os.remove('outputfile')
