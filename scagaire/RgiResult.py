
class RgiResult:
    def __init__(self, header = []):
        self.orf_id = None
        self.contig = None
        self.start = None
        self.end = None
        self.orientation = None
        self.cut_off = None
        self.pass_bitscore = None
        self.best_hit_bitscore = None
        self.gene = None
        self.best_identities = None
        self.aro = None
        self.model_type = None
        self.snps_in_best_hit_aro = None
        self.other_snps = None
        self.drug_class = None
        self.resistance_mechanism = None
        self.amr_gene_family = None
        self.predicted_dna = None
        self.predicted_protein = None
        self.card_protein_sequence = None
        self.percentage_length_of_reference_sequence = None
        self.id = None
        self.model_id = None
        self.nudged = None
        self.note = None
        
        self.header = header
        self.delimiter = "\t"

    def __str__(self):
        return (self.delimiter).join([self.orf_id, self.contig, self.start, self.end, self.orientation, self.cut_off, self.pass_bitscore, self.best_hit_bitscore, self.gene, self.best_identities, self.aro, self.model_type, self.snps_in_best_hit_aro, self.other_snps, self.drug_class, self.resistance_mechanism, self.amr_gene_family, self.predicted_dna, self.predicted_protein, self.card_protein_sequence, self.percentage_length_of_reference_sequence, self.id, self.model_id, self.nudged, self.note 
        ])
        
        
          

