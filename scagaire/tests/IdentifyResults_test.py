import unittest
import os
import shutil
from scagaire.IdentifyResults  import IdentifyResults

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','identify_results')

class TestIdentifyResults(unittest.TestCase):
    
    def test_abricate_results(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.abricate'), False).get_results()

        self.assertEqual(str(a[0]), "assembly.fasta	contig_10165	108800	110741	+	tet(M)	1-1920/1920	========/======	36/40	99.53	97.18	ncbi	NG_048232.1	tetracycline resistance ribosomal protection protein Tet(M)	TETRACYCLINE")
           

