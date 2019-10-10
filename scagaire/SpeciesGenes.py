
class SpeciesGenes:
    def __init__(self, species, gene, occurances):
        self.species    = species
        self.gene       = gene
        self.occurances = occurances
        self.delimiter  = "\t"

    def __str__(self):
        return (self.delimiter).join([self.species, self.gene, str(self.occurances) ])
                