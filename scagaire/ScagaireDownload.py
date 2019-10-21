import re
import os
import subprocess
import shutil
import pkg_resources
from tempfile import mkdtemp

from scagaire.MashSpecies import MashSpecies
from scagaire.AbricateAmrResults import AbricateAmrResults
from scagaire.SpeciesDatabase import  SpeciesDatabase

class ScagaireDownload:
    def __init__(self, options):
        self.species = options.species
        self.output_file = options.output_file
        self.output_directory = options.output_directory
        self.threads = options.threads
        self.refseq_category = options.refseq_category
        self.assembly_level = options.assembly_level
        self.mash_database = options.mash_database
        self.min_coverage = options.min_coverage
        self.min_identity = options.min_identity
        self.downloads_directory = options.downloads_directory
        self.abricate_database = options.abricate_database
        self.verbose = options.verbose
        self.debug = options.debug
        self.minimum_distance = options.minimum_distance
        
        if self.output_directory is None:
            self.output_directory = re.sub("[^a-zA-Z0-9]+", "_", self.species)

        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            
        if self.mash_database is None:
            self.mash_database = str(pkg_resources.resource_filename( __name__, 'data/refseq_reference_20191018.msh'))
        
        self.directories_to_cleanup = []

    def run(self):
        download_directory = self.downloads_directory
        if self.downloads_directory is None:
            download_directory = self.download_species()
        
        input_files = self.find_input_files(download_directory)
        filtered_input_files = self.remove_species_mismatch(input_files, self.species)
        files_to_amr_results = self.amr_for_input_files(filtered_input_files)
        gene_to_freq = self.aggregate_amr_results(files_to_amr_results)
        SpeciesDatabase(self.output_file, self.species, self.abricate_database ).output_genes_to_freq_file(gene_to_freq)
        
    def aggregate_amr_results(self, files_to_amr_results):
        gene_to_freq = {}
        for amr_results in files_to_amr_results.values():
            for amr_result in amr_results:
                if amr_result.gene in gene_to_freq:
                    gene_to_freq[amr_result.gene] += 1
                else:
                    gene_to_freq[amr_result.gene] = 1
        return gene_to_freq

    def download_species(self):
        download_directory = str(mkdtemp(dir=self.output_directory))
        self.directories_to_cleanup.append(download_directory)

        cmd = " ".join(
            [
                "ncbi-genome-download",
                "-o",
                download_directory,
                "--genus",
                '"' + self.species + '"',
                "--parallel",
                str(self.threads),
                "--assembly-level",
                self.assembly_level,
                "-R",
                self.refseq_category,
                "-F",
                "fasta",
                "bacteria",
            ]
        )
        if self.verbose:
            print("Download genomes from NCBI:\t"+ cmd)
        subprocess.check_output(cmd, shell=True)
        return download_directory
        
    def find_input_files(self, download_directory):
        input_files = []
        for root, dirs, files in os.walk(download_directory):
            for file in files:
                if file.endswith("genomic.fna.gz"):
                    input_files.append(os.path.join(root, file))
        return input_files
        
    def remove_species_mismatch(self, input_files, species):
        filtered_input_files = []
        for f in input_files:
            mash_species = MashSpecies(f, self.mash_database, self.verbose, minimum_distance = self.minimum_distance).get_species()
            if mash_species == species:
                if self.verbose:
                    print('Species match for file ' + str(f) + " got " + mash_species)
                filtered_input_files.append(f)
            else:
                if self.verbose:
                    if mash_species is not None:
                        print('Species mismatch for file ' + str(f) + ", expected " + species + " but got " + mash_species)
                    else:
                        print('Couldnt find any species for file ' + str(f) + ", expected " + species)
                
        return filtered_input_files
        
    def amr_for_input_files(self, input_files):
        files_to_amr_results = {}
        for f in input_files:
            amr = AbricateAmrResults(f, self.abricate_database, self.min_coverage, self.min_identity, self.verbose, self.threads).get_amr_results()
            files_to_amr_results[f] = amr
        return files_to_amr_results
        
    def __del__(self):
        if not self.debug:
            for d in self.directories_to_cleanup:
                if os.path.exists(d):
                    shutil.rmtree(d)
                    
                    
