import csv
import re
import os
from tempfile import mkstemp
from scagaire.RgiResult import RgiResult
from scagaire.parser.AmrParser import AmrParser

class Rgi(AmrParser):
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose

        self.minimum_num_columns = 25
        
        self.default_header = [ 'ORF_ID', 'Contig', 
        'Start', 'Stop', 'Orientation', 'Cut_Off', 
        'Pass_Bitscore', 'Best_Hit_Bitscore', 
        'Best_Hit_ARO', 'Best_Identities', 
        'ARO', 'Model_type', 'SNPs_in_Best_Hit_ARO', 
        'Other_SNPs', 'Drug Class', 
        'Resistance Mechanism', 'AMR Gene Family', 
        'Predicted_DNA', 'Predicted_Protein', 
        'CARD_Protein_Sequence', 'Percentage Length of Reference Sequence', 
        'ID', 'Model_ID', 'Nudged', 'Note']
        self.header = self.default_header
        self.column_to_variable_mapping = {
            'ORF_ID': 'orf_id',
            'Contig': 'contig',
            'Start': 'start',
            'Stop': 'end',
            'Orientation': 'orientation',
            'Cut_Off': 'cut_off',
            'Pass_Bitscore': 'pass_bitscore',
            'Best_Hit_Bitscore': 'best_hit_bitscore',
            'Best_Hit_ARO': 'gene',
            'Best_Identities': 'best_identities',
            'ARO': 'aro',
            'Model_type': 'model_type',
            'SNPs_in_Best_Hit_ARO': 'snps_in_best_hit_aro',
            'Other_SNPs': 'other_snps',
            'Drug Class': 'drug_class',
            'Resistance Mechanism': 'resistance_mechanism',
            'AMR Gene Family': 'amr_gene_family',
            'Predicted_DNA': 'predicted_dna',
            'Predicted_Protein': 'predicted_protein',
            'CARD_Protein_Sequence': 'card_protein_sequence',
            'Percentage Length of Reference Sequence': 'percentage_length_of_reference_sequence',
            'ID': 'id',
            'Model_ID': 'model_id',
            'Nudged': 'nudged',
            'Note': 'note'
        }
        self.results = self.populate_results()
        
    def populate_results(self):
        file_contents = self.read_file_multi_delimiters()
        self.header = self.get_header(file_contents)
        
        results = []
        
        for row in file_contents:
            if len(row)< self.minimum_num_columns:
                continue
            ab_result = RgiResult(header = self.default_header)
            for index, value in enumerate(row):
                if self.header[index] in self.column_to_variable_mapping:
                    variable_name = self.column_to_variable_mapping[self.header[index]]
                    
                    setattr(ab_result, variable_name, value)
                else:
                    # we couldnt work out which column it maps to
                    continue
            results.append(ab_result)
        return results

                