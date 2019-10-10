from scagaire.parser.Abricate import Abricate

class IdentifyResults:
    def __init__(self, input_file, verbose):
        self.input_file = input_file
        self.verbose = verbose

    def get_results(self):
        a = Abricate(self.input_file, self.verbose)
        # TODO allow for lots of different results files and guess which one the results belong to
        if a.is_valid():
            return a.results
        else:
            return []
    
            