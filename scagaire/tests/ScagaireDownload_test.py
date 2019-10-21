import unittest
import os
import shutil
import filecmp
from scagaire.ScagaireDownload import ScagaireDownload
from scagaire.SpeciesDatabase import SpeciesDatabase

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, "data", "scagaire_download")

class TestOptions:
    def __init__( self,species, output_file, output_directory, min_coverage, min_identity, downloads_directory  ):
        self.species = species
        self.output_file = output_file
        self.output_directory = output_directory
        self.min_coverage = min_coverage
        self.min_identity = min_identity
        self.downloads_directory = downloads_directory
        
        self.abricate_database = 'ncbi'
        self.verbose = False
        self.threads = 1
        self.minimum_distance = 1
        self.refseq_category = 'all'
        self.assembly_level = 'all'
        self.mash_database = None
        self.debug = False


class TestScagaireDownload(unittest.TestCase):
    def test_normal(self):
        g = ScagaireDownload(
            TestOptions( 'Salmonella enterica', 'outputfile', 'outputdir', 95, 95, data_dir)
        )
        
        input_files = g.find_input_files(data_dir)
        self.assertEqual([os.path.basename(f) for f in input_files ], ['xdr_genomic.fna.gz'])
        
        filtered_input_files = g.remove_species_mismatch(input_files, 'Salmonella enterica')
        self.assertEqual([os.path.basename(f) for f in filtered_input_files ], ['xdr_genomic.fna.gz'])
        
        files_to_amr_results = g.amr_for_input_files(filtered_input_files)
        amr_results = [f for f in files_to_amr_results.values()][0]
        self.assertEqual(sorted([a.gene for a in amr_results]), ['blaCTX-M-15', 'blaTEM-1', 'qnrS1'])
        
        gene_to_freq = g.aggregate_amr_results(files_to_amr_results)
        self.assertEqual(gene_to_freq, {'blaCTX-M-15':1, 'blaTEM-1':1, 'qnrS1':1})
        
        SpeciesDatabase("output_file", 'Salmonella enterica', 'ncbi', fixed_time ='20101010' ).output_genes_to_freq_file(gene_to_freq)

        self.assertTrue(os.path.exists("output_file"))
        self.assertTrue(
            filecmp.cmp(os.path.join(data_dir, "expected_output_file"), "output_file")
        )
        os.remove("output_file")
