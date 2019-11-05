import csv
import re
import os
from tempfile import mkstemp
from scagaire.IdentifyResults import IdentifyResults
from scagaire.parser.SpeciesToGenes import SpeciesToGenes

class FilterResults:
    def __init__(self, results_filename, database_filename, minimum_occurances, results_type,  database_name, verbose):
        self.results_filename = results_filename
        self.database_filename = database_filename
        self.minimum_occurances = minimum_occurances
        self.database_name = database_name
        self.results_type = results_type
        self.verbose = verbose

    def filter_by_species(self, species):
        all_results = IdentifyResults(self.results_filename, self.results_type, self.verbose).get_results()
        species_genes = SpeciesToGenes(self.database_filename, self.verbose).filter_by_species(species, self.database_name)
    
        # put the gene names in a dictionary for quick lookup 
        # and filter out low occuring genes.
        species_genes_to_occurances = { g.gene: g.occurances for g in species_genes if g.occurances >= self.minimum_occurances }
        filtered_results = [r for r in all_results if r.gene in species_genes_to_occurances]
        return filtered_results
        