
class AbricateResult:
    def __init__(self):
        self.file          = None
        self.sequence      = None
        self.start         = None
        self.end           = None
        self.strand        = None
        self.gene          = None
        self.coverage      = None
        self.coverage_map  = None
        self.gaps          = None
        self.perc_coverage = None
        self.perc_identity = None
        self.database      = None
        self.accession     = None
        self.product       = None
        self.resistance    = None
        self.delimiter = "\t"

    def __str__(self):
        return (self.delimiter).join([self.file, self.sequence, self.start, self.end, self.strand, self.gene, self.coverage, self.coverage_map, self.gaps, self.perc_coverage, self.perc_identity, self.database, self.accession, self.product, self.resistance 
        ])
        
        
          