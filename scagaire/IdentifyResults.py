from scagaire.parser.Abricate098 import Abricate098
from scagaire.parser.Abricate097 import Abricate097
from scagaire.parser.Staramr import Staramr
from scagaire.parser.Rgi import Rgi

class IdentifyResults:
    def __init__(self, input_file, results_type, verbose):
        self.input_file = input_file
        self.results_type = results_type
        self.verbose = verbose

    # Refactor when we get more result formats
    def get_results(self):
        a = Abricate098(self.input_file, self.verbose)
        if a.is_valid():
            return a.results
            
        a7 = Abricate097(self.input_file, self.verbose)
        if a7.is_valid() or self.results_type == 'abricate':
            return a7.results
        
        s = Staramr(self.input_file, self.verbose)
        if s.is_valid() or self.results_type == 'staramr':
            return s.results
            
        r = Rgi(self.input_file, self.verbose)
        if r.is_valid() or self.results_type == 'rgi':
            return r.results

        return []
                  