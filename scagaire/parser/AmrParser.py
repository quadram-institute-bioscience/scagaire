import csv
import re
import os
from tempfile import mkstemp

class AmrParser:
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose
        self.minimum_num_columns = 1
        self.default_header = [ ]
        self.column_to_variable_mapping = {}

    def is_valid(self):
        for i,h in enumerate(self.header):
            if h != self.default_header[i]:
                return False
        
        return True
        
    def get_header(self, file_contents):
        return file_contents.pop(0)
        
    def read_file_multi_delimiters(self):
        file_contents = []
        with open(self.input_file, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.readline(), [',','\t'])
            csvfile.seek(0)
            bnreader = csv.reader(csvfile, dialect)
            
            for row in bnreader:
                file_contents.append(row)

        return file_contents
                