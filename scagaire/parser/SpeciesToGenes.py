import csv
import re
import os
from tempfile import mkstemp
from scagaire.SpeciesGenes import SpeciesGenes

class SpeciesToGenes:
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose
        self.minimum_num_columns = 3

        self.species_to_genes = self.populate()
        
    def read_file_multi_delimiters(self):
        file_contents = []
        with open(self.input_file, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.readline(), [',','\t'])
            csvfile.seek(0)
            bnreader = csv.reader(csvfile, dialect)
            
            header  = next(bnreader)
            for row in bnreader:
                file_contents.append(row)

        return file_contents
                
    def populate(self):
        file_contents = self.read_file_multi_delimiters()
        results = []
        
        for row in file_contents:
            if len(row)< self.minimum_num_columns:
                continue
            results.append(SpeciesGenes(str(row[0]), str(row[1]), int(row[2]), str(row[4])))
        return results
    
    def all_species(self):
        return sorted(list(set([s.species for s in self.species_to_genes])))
        
    def filter_by_species(self, query, database_name):
        return [s for s in self.species_to_genes if s.species == query and s.database_name == database_name]
            
            