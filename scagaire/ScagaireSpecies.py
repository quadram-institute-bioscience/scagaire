import os
import pkg_resources
from scagaire.parser.SpeciesToGenes  import SpeciesToGenes
from scagaire.Config import Config

class ScagaireSpecies:
    def __init__(self, verbose, detailed, overview, database_filename = 'species_to_genes.tsv'):
        self.verbose = verbose
        self.database_filename = database_filename
        self.detailed = detailed
        self.overview = overview
        # look up the bundled database
        self.database = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), self.database_filename)
    
        self.config_file = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), 'config.json')
    
    def print_all(self):
        if self.overview:
            self.print_overview()
        elif self.detailed:
            self.print_detailed()
        else:
            self.print_simple()
        
        
    def print_overview(self):
        sg = SpeciesToGenes(self.database, self.verbose)
        databases = sorted(sg.all_databases())
        print("No. of species:\t" + str(sg.num_of_all_species()))
        print("No. of databases:\t" + str(sg.num_of_all_databases()))
        print("No. of genes:\t" + str(sg.num_of_all_genes()))
        print("Sum of occurances:\t" + str(sg.sum_of_occurances()))
    
    def print_detailed(self):
        sg = SpeciesToGenes(self.database, self.verbose)
        databases = sorted(sg.all_databases())
        # header
        print("\t".join(['Species'] + databases))

        for species in sorted(sg.all_species()):
            species_dbs = sg.species_databases(species)
            cells = [species]
            for d in databases:
                if d in species_dbs:
                    cells.append(d)
                else:
                    cells.append('----')
            print("\t".join(cells))
            
        
    def print_simple(self):
        sg = SpeciesToGenes(self.database, self.verbose)
        print("\n".join(sorted(sg.all_species())))

        c = Config(self.config_file, self.verbose)
        print("\n".join(c.taxon_categories_printable_list()))
