import csv
import re
import os
from tempfile import mkstemp
from scagaire.IdentifyResults import IdentifyResults
from scagaire.parser.SpeciesToGenes import SpeciesToGenes

class FilterResults:
    def __init__(self, results_filename, database_filename, species, minimum_occurances, verbose):
        self.results_filename = results_filename
        self.database_filename = database_filename
        self.species = species
        self.minimum_occurances = minimum_occurances
        self.verbose = verbose

    def filter_by_species(self):
        all_results = IdentifyResults(self.results_filename, self.verbose).get_results()
        species_genes = SpeciesToGenes(self.database_filename, self.verbose).filter_by_species(self.species)
    
        # put the gene names in a dictionary for quick lookup 
        # and filter out low occuring genes.
        species_genes_to_occurances = { g.gene: g.occurances for g in species_genes if g.occurances >= self.minimum_occurances }
        filtered_results = [r for r in all_results if r.gene in species_genes_to_occurances]
        return filtered_results
        