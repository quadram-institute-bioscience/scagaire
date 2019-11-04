import unittest
import os
import shutil
import filecmp
from scagaire.Scagaire import Scagaire

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, "data", "scagaire")

class TestOptions:
    def __init__( self, input_file, minimum_occurances, output_file, results_type, summary_file, overwrite_files, species ):
        self.input_file = input_file
        self.minimum_occurances = minimum_occurances
        self.output_file = output_file
        self.results_type = results_type
        self.summary_file = summary_file
        self.overwrite_files = overwrite_files
        self.species = species
        self.database_name = 'ncbi'
        self.database_file = os.path.join(data_dir, 'database.tsv')
        self.verbose = False

class TestScagaire(unittest.TestCase):
    def test_abricate098(self):
        self.cleanup()
        s = Scagaire(
            TestOptions( os.path.join(data_dir, 'results.abricate098'), 0, 'output_file', None, 'summary_file', False, 'Escherichia coli' ))
        s.run()
        self.assertTrue(os.path.exists('output_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate098_output_file"), "output_file")
        )
        
        self.assertTrue(os.path.exists('summary_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate098_summary_file"), "summary_file")
        )
        
        self.cleanup()
       
    def test_abricate097_no_result(self):
        self.cleanup()
        s = Scagaire(
            TestOptions( os.path.join(data_dir, 'results.abricate097'), 0, 'output_file', None, 'summary_file', False, 'Escherichia coli' ))
        s.run()
        self.assertTrue(os.path.exists('output_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate097_no_result_output_file"), "output_file")
        )
        
        self.assertTrue(os.path.exists('summary_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate097_no_result_summary_file"), "summary_file")
        )     
        self.cleanup()

    def test_abricate097_staph(self):
        self.cleanup()
        s = Scagaire(
            TestOptions( os.path.join(data_dir, 'results.abricate097'), 0, 'output_file', None, 'summary_file', False, 'Staphylococcus aureus' ))
        s.run()
        self.assertTrue(os.path.exists('output_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate097_staph_output_file"), "output_file")
        )
        
        self.assertTrue(os.path.exists('summary_file'))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_abricate097_staph_summary_file"), "summary_file")
        ) 
        self.cleanup()
        
    def cleanup(self):
        for f in ['summary_file', 'output_file']:
            if os.path.exists(f):
                os.remove(f)
        
        