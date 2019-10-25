
import os
import sys
import pkg_resources
from scagaire.FilterResults import FilterResults
from scagaire.Config import Config
from scagaire.parser.SpeciesToGenes import SpeciesToGenes
from scagaire.Summary import Summary

class Scagaire:
    def __init__(self, options):
        self.verbose = options.verbose
        self.input_file = options.input_file
        self.database = options.database
        self.minimum_occurances = options.minimum_occurances
        self.output_file = options.output_file
        self.results_type = options.results_type
        self.summary_file = options.summary_file
        self.overwrite_files = options.overwrite_files
        
        if self.database is None:
            self.database = str(pkg_resources.resource_filename( __name__, 'data/species_to_genes.tsv'))
            
        self.config_file = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), 'config.json')
        self.species = self.parse_species(options.species)
        
        if self.overwrite_files:
            if self.output_file is not None and os.path.exists(self.output_file):
                os.remove(self.output_file)
            if self.summary_file is not None and os.path.exists(self.summary_file):
                os.remove(self.output_file)
        else:            
            if self.output_file is not None and os.path.exists(self.output_file):
                sys.exit("Output file already exists, please choose another filename.")
            if self.summary_file is not None and os.path.exists(self.summary_file):
                sys.exit("Summary file already exists, please choose another filename.")
            
    # allow for "Salmonella enterica", 
    # "Salmonella enterica,Streptococcus pneumoniae", 
    # "Salmonella enterica,skin"
    def parse_species(self, species_str):
        config = Config(self.config_file, self.verbose)
        split_species_str = species_str.split(",")
        output_species = []
        for s in split_species_str:
            if s in config.taxon_categories():
                for c in config.taxon_categories()[s]:
                    output_species.append(c)
            else:
                output_species.append(s)
        return output_species
        
    def output_summary(self, results, species):
        s = Summary(results, self.verbose)
        output_gene_occurances = [str(g) for g in s.aggregate_results().values()]
        
        with open(self.summary_file, "a+") as output_fh:
            if len(results) > 0:
                for r in output_gene_occurances:
                    output_fh.write(species + "\t" + r + "\n")
            else:
                output_fh.write(species + "\t" + "no_results\t0" + "\n")

    def run(self):
        filter_results =  FilterResults(self.input_file, self.database, self.minimum_occurances, self.results_type, self.verbose)
        
        sg = SpeciesToGenes(self.database, self.verbose)
        for spec in self.species:
        
            if spec not in sg.all_species():
                print("Error: Species not found in database so nothing to do")
                return

            results = filter_results.filter_by_species(spec)
            self.output_summary(results, spec)
            
            output_content = "\n".join([str(r) for r in results])
            header = ""
            if len(results) > 0:
                header = "\t".join(results[0].header)
            else:
                header = "No results"
            
            if self.output_file != None:
                with open(self.output_file, "a+") as output_fh:
                    if len(self.species) > 1:
                        output_fh.write("Results for species:\t" + str(spec) + "\n=======================\n")
                    output_fh.write(header+ "\n")
                    output_fh.write(output_content + "\n")
            else:
                print("Results for species:\t" + str(spec) + "\n=======================")
                print(header)
                print(output_content)
        