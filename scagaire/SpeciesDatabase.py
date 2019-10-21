import os
import sys
from datetime import datetime

class SpeciesDatabase:
    def __init__(self, output_file, species, database, fixed_time = None):
        self.species    = species
        self.output_file = output_file
        self.database = database
        self.fixed_time = fixed_time
        self.delimiter  = "\t"

    #Campylobacter jejuni	blaOXA-785	6	manual_ncbi_website	20191008
    def output_genes_to_freq_file(self, gene_to_freq):
        with open(self.output_file, "w") as out_fh:
            for gene, freq in gene_to_freq.items():
                gene_results = [self.species, gene, str(freq), 'abricate_' + self.database + '_auto']
                
                if self.fixed_time is None:
                    gene_results.append(datetime.today().strftime('%Y%m%d'))
                else:
                    gene_results.append(self.fixed_time)
                out_fh.write( self.delimiter.join([str(g) for g in gene_results]) + "\n")
                