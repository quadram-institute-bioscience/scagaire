
class SpeciesGenes:
    def __init__(self, species, gene, occurances, database_name):
        self.species    = species
        self.gene       = gene
        self.occurances = occurances
        self.database_name = database_name
        self.delimiter  = "\t"

    def __str__(self):
        return (self.delimiter).join([self.species, self.gene, str(self.occurances), self.database_name ])
                