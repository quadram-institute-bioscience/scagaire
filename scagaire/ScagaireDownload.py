import re
import os
import subprocess
import shutil
from tempfile import mkdtemp
from scagaire.MashSpecies import MashSpecies

class ScagaireDownload:
    def __init__(self, options):
        self.species = options.species
        self.output_file = options.output_file
        self.threads = options.threads
        self.refseq_category = options.refseq_category
        self.assembly_level = options.assembly_level
        self.verbose = options.verbose
        
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
        filtered_input_files = self.remove_species_mismatch(input_files)
        
        # ncbi downloader
        # Check species
        # run abricate
        # filter abricate genes
        # aggregate genes
        # output
        
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
            mash_species = MashSpecies(f, self.mash_database).get_species()
            if mash_species == species:
                filtered_input_files.append(f)
            else:
                if self.verbose:
                    print('Species mismatch for file ' + str(f) + ", expected " + species + " but got " + mash_species)
                
        return filtered_input_files
        
    def __del__(self):
        if not self.debug:
            for d in self.directories_to_cleanup:
                if os.path.exists(d):
                    shutil.rmtree(d)