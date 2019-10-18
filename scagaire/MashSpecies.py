import os
import subprocess

class MashSpecies:
    def __init__(self, input_file, database, verbose, minimum_distance = 0.1):
        self.input_file = input_file
        self.database = database
        self.minimum_distance = minimum_distance
        self.verbose = verbose
        
    def get_species(self):
        cmd = " ".join(['mash', 'dist','-d', '0.1', self.database, self.input_file, '|', 'sort','-k', '3', '|', 'head', '-n', '1'])
        if self.verbose:
            print("Run Mash against RefSeq reference genomes\t"+ cmd)
        mash_output = subprocess.check_output(cmd, shell=True)
        
        if len(mash_output) > 0:
            sketch_match = mash_output.split('/')
            species = sketch_match[1]." ".sketch_match[2]
            return species
        return None
        