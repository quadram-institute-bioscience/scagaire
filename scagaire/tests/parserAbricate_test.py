import unittest
import os
import shutil
from scagaire.parser.Abricate  import Abricate

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','parser','abricate')

class TestAbricate(unittest.TestCase):
    
    def test_header_only(self):
        a = Abricate(os.path.join(data_dir, 'header_only.abricate'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(a.results, [])
        
    # check you get the same results if its comma or tab delimited
    def test_comma_separated(self):
        a = Abricate(os.path.join(data_dir, 'comma_separated.csv'), False)
        t = Abricate(os.path.join(data_dir, 'tab_separated.tsv'), False)
        self.assertEqual(a.read_file_multi_delimiters(), t.read_file_multi_delimiters())
        self.assertEqual(len(a.read_file_multi_delimiters()[0]), 15)
        self.assertEqual(str(a.populate_results()[0]), "assembly.fasta	contig_10165	108800	110741	+	tet(M)	1-1920/1920	========/======	36/40	99.53	97.18	ncbi	NG_048232.1	tetracycline resistance ribosomal protection protein Tet(M)	TETRACYCLINE")
           
    def test_metagenomic_results(self):
        a = Abricate(os.path.join(data_dir, 'metagenomic_results.abricate'), False)
        self.assertTrue(a.is_valid())
        self.assertEqual(len(a.results), 137)
