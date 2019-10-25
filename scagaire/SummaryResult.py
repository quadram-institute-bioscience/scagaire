class SummaryResult:
    
    def __init__(self, gene_name, occurances):
        self.gene_name = gene_name
        self.occurances = occurances
        
    def __str__(self):
        return "\t".join([self.gene_name, str(self.occurances )])
        