from scagaire.parser.Abricate import Abricate
from scagaire.parser.Staramr import Staramr

class IdentifyResults:
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose

    # Refactor when we get more result formats
    def get_results(self):
        a = Abricate(self.input_file, self.verbose)
        if a.is_valid():
            return a.results
        
        s = Staramr(self.input_file, self.verbose)
        if s.is_valid():
            return s.results

        return []
                  