import csv
import re
import os
from tempfile import mkstemp
from scagaire.AbricateResult097 import AbricateResult097
from scagaire.parser.AmrParser import AmrParser

class Abricate097(AmrParser):
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose

        self.minimum_num_columns = 13
        self.default_header = [ '#FILE', 'SEQUENCE', 'START', 'END', 'GENE', 'COVERAGE', 'COVERAGE_MAP', 'GAPS', '%COVERAGE', '%IDENTITY', 'DATABASE', 'ACCESSION', 'PRODUCT']
        self.header = self.default_header
        self.column_to_variable_mapping = {
            '#FILE': 'file', 
            'SEQUENCE': 'sequence', 
            'START': 'start', 
            'END': 'end', 
            'GENE': 'gene', 
            'COVERAGE': 'coverage', 
            'COVERAGE_MAP': 'coverage_map', 
            'GAPS': 'gaps', 
            '%COVERAGE': 'perc_coverage', 
            '%IDENTITY': 'perc_identity', 
            'DATABASE': 'database', 
            'ACCESSION': 'accession', 
            'PRODUCT': 'product'
        }
        self.results = self.populate_results()
        
    def populate_results(self):
        file_contents = self.read_file_multi_delimiters()
        self.header = self.get_header(file_contents)
        
        abricate_results = []
        
        for row in file_contents:
            if len(row)< self.minimum_num_columns:
                continue
            ab_result = AbricateResult097(header = self.default_header)
            for index, value in enumerate(row):
                if self.header[index] in self.column_to_variable_mapping:
                    variable_name = self.column_to_variable_mapping[self.header[index]]
                    
                    setattr(ab_result, variable_name, value)
                else:
                    # we couldnt work out which column it maps to
                    continue
            abricate_results.append(ab_result)
        return abricate_results
        
    def __str__(self):
        return "\n".join([str(r) for r in self.results])
            

                