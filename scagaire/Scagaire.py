
import os
import sys
import pkg_resources
from scagaire.FilterResults import FilterResults
from scagaire.parser.SpeciesToGenes import SpeciesToGenes

class Scagaire:
    def __init__(self, options):
        self.input_file = options.input_file
        self.species = options.species
        self.database = options.database
        self.minimum_occurances = options.minimum_occurances
        self.output_file = options.output_file
        self.results_type = options.results_type
        self.verbose = options.verbose

        if self.database is None:
            self.database = str(pkg_resources.resource_filename( __name__, 'data/species_to_genes.tsv'))

    def run(self):
        filter_results =  FilterResults(self.input_file, self.database, self.minimum_occurances, self.results_type, self.verbose)
        
        sg = SpeciesToGenes(self.database, self.verbose)
        if self.species not in sg.all_species():
            print("Error: Species not found in database so nothing to do")
            return
        
        results = filter_results.filter_by_species(self.species)
        output_content = "\n".join([str(r) for r in results])
        
        if self.output_file != None:
            with open(self.output_file, "w+") as output_fh:
                output_fh.write(output_content)
        else:
            print(output_content)
        