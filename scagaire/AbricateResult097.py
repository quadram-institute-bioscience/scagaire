
class AbricateResult097:
    def __init__(self, header = []):
        self.file          = None
        self.sequence      = None
        self.start         = None
        self.end           = None
        self.gene          = None
        self.coverage      = None
        self.coverage_map  = None
        self.gaps          = None
        self.perc_coverage = None
        self.perc_identity = None
        self.database      = None
        self.accession     = None
        self.product       = None
        
        self.header = header
        self.delimiter = "\t"

    def __str__(self):
        return (self.delimiter).join([self.file, self.sequence, self.start, self.end, self.gene, self.coverage, self.coverage_map, self.gaps, self.perc_coverage, self.perc_identity, self.database, self.accession, self.product
        ])
