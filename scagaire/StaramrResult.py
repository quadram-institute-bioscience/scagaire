
class StaramrResult:
    def __init__(self, header = []):
        self.file          = None
        self.sequence      = None
        self.start         = None
        self.end           = None
        self.gene          = None
        self.coverage      = None
        self.perc_coverage = None
        self.perc_identity = None
        self.accession     = None
        self.resistance    = None
        
        self.header = header
        self.delimiter = "\t"

    def __str__(self):
        return (self.delimiter).join([self.file, self.gene, self.resistance, self.perc_identity, self.perc_coverage, self.coverage, self.sequence, self.start, self.end, self.accession ])
