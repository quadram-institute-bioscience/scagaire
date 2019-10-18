import csv
import re
import os
from tempfile import mkstemp
from scagaire.StaramrResult import StaramrResult
from scagaire.parser.AmrParser import AmrParser

class Staramr(AmrParser):
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose

        self.minimum_num_columns = 10

        self.default_header = [ 'Isolate ID', 'Gene','Predicted Phenotype', '%Identity', '%Overlap', 'HSP Length/Total Length', 'Contig', 'Start', 'End', 'Accession']
        self.header = self.default_header
        
        self.column_to_variable_mapping = {
            'Isolate ID': 'file',
            'Gene': 'gene',
            'Predicted Phenotype': 'resistance',
            '%Identity': 'perc_identity', 
            '%Overlap': 'perc_coverage', 
            'HSP Length/Total Length': 'coverage', 
            'Contig': 'sequence', 
            'Start': 'start',
            'End': 'end', 
            'Accession': 'accession'
        }
        self.results = self.populate_results()
        
    def populate_results(self):
        file_contents = self.read_file_multi_delimiters()
        self.header = self.get_header(file_contents)
        
        staramr_results = []
        
        for row in file_contents:
            if len(row)< self.minimum_num_columns:
                continue
            ab_result = StaramrResult(header = self.default_header)
            for index, value in enumerate(row):
                if self.header[index] in self.column_to_variable_mapping:
                    variable_name = self.column_to_variable_mapping[self.header[index]]
                    
                    setattr(ab_result, variable_name, value)
                else:
                    # we couldnt work out which column it maps to
                    continue
            staramr_results.append(ab_result)
        return staramr_results
                