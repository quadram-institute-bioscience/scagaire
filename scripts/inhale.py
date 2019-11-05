#!/usr/bin/env python3
import sys
sys.path.append('../')
sys.path.append('./')
import argparse
import os
import re
import csv
import shutil
from scagaire.Scagaire import Scagaire

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, "..","scagaire","tests", "data", "scagaire", "natbiotech")

class TestOptions:
    def __init__( self, input_file, minimum_occurances, output_file, results_type, summary_file, overwrite_files, species, database_name  ):
        self.input_file = input_file
        self.minimum_occurances = minimum_occurances
        self.output_file = output_file
        self.results_type = results_type
        self.summary_file = summary_file
        self.overwrite_files = overwrite_files
        self.species = species
        self.database_name = database_name
        self.database_file = None
        self.verbose = False
        
class SampleAMR:
    def __init__(self,  sample_name, species, amr_genes):
        self.sample_name = sample_name
        self.species = species.split(",")
        self.amr_genes = amr_genes

class Inhale():
    def run_analysis(self, database_name):
        self.cleanup()
        
        samples = self.read_sample_amr(os.path.join(data_dir, 'sample_amr'))
        
        for sample in samples.values():
            self.extract_results(sample.sample_name, database_name, os.path.join(data_dir, 'all_results.abricate'), 'filtered_results') 
                 
            for spec in sample.species:
                
                output_suffix = '_' +sample.sample_name +"_" + spec + "_" + database_name
                output_suffix = re.sub("[^a-zA-Z0-9]+", "_", output_suffix)
                summary_file = 'summary_file' + output_suffix
                s = Scagaire(
                    TestOptions(  'filtered_results', 0, 'output_file', None, summary_file, False, spec, database_name))
                s.run()
                if not os.path.exists(summary_file):
                    continue
                
                summary_contents = []
                with open(summary_file, newline='') as csvfile:
                    dialect = csv.Sniffer().sniff(csvfile.readline(), ['\t'])
                    csvfile.seek(0)
                    bnreader = csv.reader(csvfile, dialect)

                    genes_to_freq = {}
                    for row in bnreader:
                        genes_to_freq[row[1]] = str(row[2])
                        
                    summary_contents = [ gene + " (" + genes_to_freq[gene]+")"  for gene in sorted(genes_to_freq.keys())]

                print( "\t".join([sample.sample_name, spec, database_name] + summary_contents) )
                for f in [ 'output_file', summary_file]:
                    if os.path.exists(f):
                        os.remove(f)
            self.cleanup()

        self.cleanup()
        
    def extract_results(self, sample_prefix, database_name, results_input_file, results_output_file):
        output_contents = []
        with open(results_input_file, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.readline(), ['\t'])
            csvfile.seek(0)
            bnreader = csv.reader(csvfile, dialect)
        
            header = next(bnreader)
            output_contents.append("\t".join(header))
            for row in bnreader:
                if re.match( sample_prefix + '-', row[0]) and row[10] == database_name:
                    output_contents.append("\t".join(row))
        
        with open(results_output_file, "+a") as out_fh:
            out_fh.write("\n".join(output_contents))
        
    def read_sample_amr(self, filename):
        samples = {}
        with open(filename, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.readline(), ['\t'])
            csvfile.seek(0)
            bnreader = csv.reader(csvfile, dialect)
        
            header  = next(bnreader)
            for row in bnreader:
                samples[row[0]] = SampleAMR(row[0], row[1], row[2:])

        return samples
        
    def print_ARMA(self):
        samples = self.read_sample_amr(os.path.join(data_dir, 'sample_amr'))
        
        for sample in samples.values():
            print( "\t".join([sample.sample_name, ",".join(sample.species), 'ARMA'] + sorted(sample.amr_genes)) )
    
    def cleanup(self):
        for f in ['summary_file', 'output_file', 'filtered_results']:
            if os.path.exists(f):
                os.remove(f)
 
 
 
i = Inhale()  
for db in ['argannot', 'card','resfinder', 'ncbi', 'plasmidfinder', 'vfdb']:
    i.run_analysis(db)
i.print_ARMA()
    
    