import json

class Config:
    def __init__(self, input_file,  verbose):
        self.input_file = input_file
        self.verbose = verbose
        self.configuration = self.read_contents()

    def read_contents(self):
        data = {}
        with open(self.input_file) as json_file:
            data = json.load(json_file)
        return data

    def taxon_categories(self):
        return self.configuration['taxon_categories']
        
    def taxon_categories_printable_list(self):
        output = []
        for category, species in self.taxon_categories().items():
            
            # Shorten the taxon names (if they have Genus species)
            shortened_genus_species = []
            for s in sorted(species):
                genus_species = s.split(" ")
                if len(genus_species)>1:
                    shortened_genus_species.append(genus_species[0][0] + ". " + genus_species[1])
                else:
                    shortened_genus_species.append(s)
            
            species_list = ", ".join(shortened_genus_species)
            output.append(category + "\t(" + species_list + ")")
        return output
            
                