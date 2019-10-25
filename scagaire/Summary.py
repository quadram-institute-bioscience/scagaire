from scagaire.SummaryResult import SummaryResult

class Summary:
    def __init__(self, results, verbose):
        self.results = results
        self.verbose = verbose

    def aggregate_results(self):
        genename_to_summary = {}
        for r in self.results:
            if r.gene in genename_to_summary:
                genename_to_summary[r.gene].occurances += 1
            else:
                genename_to_summary[r.gene] = SummaryResult(r.gene, 1)
        return genename_to_summary 
