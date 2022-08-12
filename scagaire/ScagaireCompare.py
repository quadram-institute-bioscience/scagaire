import os
import pkg_resources
from scagaire.parser.SpeciesToGenes  import SpeciesToGenes
from scagaire.Config import Config

class ScagaireCompare:
    def __init__(self, options):
        self.verbose  = options.verbose
        self.debug    = options.debug
        self.verbose = options.verbose
        
        self.species1 = options.species1
        self.species2 = options.species2
        self.database_filter = options.database_filter
        # look up the bundled database
        self.database = options.database_file
        
        if options.database_file is None:
            self.database = str(pkg_resources.resource_filename( __name__, 'data/species_to_genes.tsv'))
    
        self.config_file = os.path.join(str(pkg_resources.resource_filename( __name__, 'data/')), 'config.json')
    

    def compare(self):
        sg = SpeciesToGenes(self.database, self.verbose)
        species1_species_to_genes = sg.filter_by_species(self.species1, self.database_filter)
        species2_species_to_genes = sg.filter_by_species(self.species2, self.database_filter)
        
        species1_gene_names = [s.gene for s in species1_species_to_genes]
        species2_gene_names = [s.gene for s in species2_species_to_genes]
        
        filtered_species1_species_to_genes = [s for s in species1_species_to_genes if s.gene in species2_gene_names]
        filtered_species2_species_to_genes = [s for s in species2_species_to_genes if s.gene in species1_gene_names]
        
        for s in filtered_species1_species_to_genes:
            matching_species = [s2 for s2 in filtered_species2_species_to_genes if s.gene == s2.gene]
            
            print("\t".join([s.gene, s.species, str(s.occurances), matching_species[0].species, str(matching_species[0].occurances)]))
            
