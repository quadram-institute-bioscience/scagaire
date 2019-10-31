import os
import subprocess
from scagaire.parser.Abricate098 import Abricate098
from tempfile import mkstemp

class AbricateAmrResults:
    def __init__(self, input_file, database_name, min_coverage, min_identity, threads, verbose):
        self.input_file = input_file
        self.database_name = database_name
        self.min_coverage = min_coverage
        self.min_identity = min_identity
        self.threads = threads
        
        self.verbose = verbose
        
    def get_amr_results(self):
        fd, abricate_output = mkstemp()
        
        cmd = " ".join(['abricate', '--db', self.database_name, '--minid', str(self.min_identity), '--mincov', str(self.min_coverage),'--threads', str(self.threads), self.input_file , '>', abricate_output])
        if self.verbose:
            print("Run Abricate to find AMR genes\t"+ cmd)
        subprocess.check_output(cmd, shell=True)
        
        ab_parser = Abricate098(abricate_output, self.verbose)
        os.close(fd)
        os.remove(abricate_output)
        if self.verbose:
            print(str(ab_parser))
        
        return ab_parser.results
        