import re
import os
import subprocess
import shutil
import pkg_resources
from tempfile import mkdtemp
from datetime import datetime
from scagaire.MashSpecies import MashSpecies
from scagaire.AbricateAmrResults import AbricateAmrResults

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
        self.abricate_database = options.abricate_database
        self.verbose = options.verbose
        self.debug = options.debug
        
        if self.output_directory is None:
            self.output_directory = re.sub("[^a-zA-Z0-9]+", "_", self.species)

        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            
        if self.mash_database is None:
            self.mash_database = str(pkg_resources.resource_filename( __name__, 'data/refseq_reference_20191018.msh'))
        
        self.directories_to_cleanup = []

    def run(self):
        download_directory = self.download_species()
        input_files = self.find_input_files(download_directory)
        filtered_input_files = self.remove_species_mismatch(input_files, self.species)
        files_to_amr_results = self.amr_for_input_files(filtered_input_files)
        gene_to_freq = self.aggregate_amr_results(files_to_amr_results)
        
    def aggregate_amr_results(self, files_to_amr_results):
        gene_to_freq = {}
        for amr_results in files_to_amr_results.values():
            if amr_results in gene_to_freq:
                gene_to_freq[amr_results] += 1
            else:
                gene_to_freq[amr_results] = 1
        return gene_to_freq
            
    #Campylobacter jejuni	blaOXA-785	6	manual_ncbi_website	20191008
    def output_genes_to_freq_file(self, gene_to_freq):
        with open(self.output_file, "w") as out_fh:
            for gene, freq in gene_to_freq.items():
                gene_results = [self.species, gene, str(freq), 'abricate_' + self.abricate_database + '_auto', datetime.today().strftime('%Y%m%d')]
                out_fh.write( "\t".join(gene_results))
        
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
            mash_species = MashSpecies(f, self.mash_database, self.verbose).get_species()
            if mash_species == species:
                if self.verbose:
                    print('Species match for file ' + str(f) + " got " + mash_species)
                filtered_input_files.append(f)
            else:
                if self.verbose:
                    print('Species mismatch for file ' + str(f) + ", expected " + species + " but got " + mash_species)
                
        return filtered_input_files
        
    def amr_for_input_files(self, input_files):
        files_to_amr_results = {}
        for f in input_files:
            amr = AbricateAmrResults(f, self.abricate_database, self.min_coverage, self.min_identity, self.verbose).get_amr_results()
            files_to_amr_results[f] = amr
        return files_to_amr_results
        
    def __del__(self):
        if not self.debug:
            for d in self.directories_to_cleanup:
                if os.path.exists(d):
                    shutil.rmtree(d)
                    
                    
