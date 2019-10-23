import os
import pkg_resources
from scagaire.parser.SpeciesToGenes  import SpeciesToGenes
from scagaire.Config import Config

class ScagaireSpecies:
    def __init__(self, verbose, database_filename = 'species_to_genes.tsv'):
        self.verbose = verbose
        self.database_filename = database_filename
        # look up the bundled database
        self.database = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), self.database_filename)
    
        self.config_file = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), 'config.json')
    
    def print_all(self):
        sg = SpeciesToGenes(self.database, self.verbose)
        print("\n".join(sorted(sg.all_species())))

        c = Config(self.config_file, self.verbose)
        print("\n".join(c.taxon_categories_printable_list()))
