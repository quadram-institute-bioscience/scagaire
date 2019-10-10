import unittest
import os
import shutil
from scagaire.parser.SpeciesToGenes  import SpeciesToGenes

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','parser','species_to_genes')

class TestSpeciesToGenes(unittest.TestCase):
    
    def test_small_valid(self):
        a = SpeciesToGenes(os.path.join(data_dir, 'small_valid.tsv'), False)
        
        output_strs = [ str(s) for s in a.species_to_genes]
        
        self.assertEqual(output_strs, 
            ["Acinetobacter baumannii\taac(2')-Ib\t85", 
            'Acinetobacter baumannii\taac(3)-I\t1144', 
            'Salmonella enterica\taac(3)-II\t18'])
            
        self.assertEqual(a.all_species(), ['Acinetobacter baumannii', 'Salmonella enterica'])
        self.assertEqual([ str(s) for s in a.filter_by_species('Salmonella enterica')], 
            ['Salmonella enterica\taac(3)-II\t18'])
        self.assertEqual([ str(s) for s in a.filter_by_species('Acinetobacter baumannii')], 
            ["Acinetobacter baumannii\taac(2')-Ib\t85", 
            'Acinetobacter baumannii\taac(3)-I\t1144'])
        
