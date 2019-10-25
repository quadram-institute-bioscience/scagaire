import unittest
import os
import shutil
import filecmp
from scagaire.Summary import Summary
from scagaire.IdentifyResults import IdentifyResults

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','summary')

class TestSummary(unittest.TestCase):
    
    def test_normal_case_abricate097(self):
        results = IdentifyResults(os.path.join(data_dir, 'results.abricate097'), None, False).get_results()
        s = Summary(results, False)
        output = [str(g) for g in s.aggregate_results().values()]
        self.assertEqual(sorted(output), 
                        sorted(['blaI_of_Z\t264',
                         'blaPC1\t1',
                         'blaR1\t77',
                         'blaR1-2\t51',
                         'blaTEM-116\t1',
                         'blaTEM-156\t1',
                         'blaZ\t231',
                         'erm(B)\t16',
                         'fosB-Saur\t60',
                         'fusC\t42',
                         'mecA\t17',
                         'tet(38)\t39',
                         'tet(M)\t5']))
                         
    def test_normal_case_abricate098(self):
        results = IdentifyResults(os.path.join(data_dir, 'results.abricate098'), None, False).get_results()
        s = Summary(results, False)
        output = [str(g) for g in s.aggregate_results().values()]
        self.assertEqual(sorted(output), 
                        sorted(["aac(6')-Im\t1", 
                        'aad9\t4', 
                        'aadE\t7', 
                        'ant(6)-Ia\t1', 
                        "aph(2'')-IIa\t1", 
                        "aph(3'')-Ib\t2", 
                        "aph(3')-IIIa\t1", 
                        'aph(6)-Id\t1', 
                        'blaACI-1\t1', 
                        'blaEC\t1', 
                        'car(A)\t1', 
                        'catA13\t2', 
                        'catB1\t1', 
                        'catP\t1', 
                        'cblA\t2', 
                        'cepA\t4', 
                        'cfr(C)\t1', 
                        'cfxA6\t1', 
                        'cfxA_gen\t1', 
                        'dfrA14\t1', 
                        'dfrF\t1', 
                        'erm(B)\t2', 
                        'erm(F)\t5', 
                        'erm(Q)\t1', 
                        'lnu(AN2)\t1', 
                        'lnu(C)\t2', 
                        'mef(A)\t1', 
                        'mef(En2)\t1', 
                        'sat4\t1', 
                        'spw\t1', 
                        'sul2\t1', 
                        'taeA\t1', 
                        'tet(32)\t3', 
                        'tet(37)\t1', 
                        'tet(40)\t2', 
                        'tet(M)\t2', 
                        'tet(O)\t13', 
                        'tet(Q)\t23', 
                        'tet(W)\t19', 
                        'tet(X)\t3', 
                        'tetA(46)\t1', 
                        'tetA(P)\t1', 
                        'tetB(P)\t1', 
                        'vanG\t1', 
                        'vanO\t4', 
                        'vanR-Cd\t1', 
                        'vanR-G\t3', 
                        'vanS-D\t1', 
                        'vanU-G\t2', 
                        'vanW-G\t2', 'vanXY-G2\t1']))
                        
    def test_normal_case_rgi(self):
        results = IdentifyResults(os.path.join(data_dir, 'results.rgi'), None, False).get_results()
        s = Summary(results, False)
        output = [str(g) for g in s.aggregate_results().values()]
        self.assertEqual(sorted(output), 
                        sorted(["APH(3'')-Ib\t2", 
                        'APH(6)-Id\t1', 
                        'sul2\t2']))     
                                           
    def test_normal_case_staramr(self):
        results = IdentifyResults(os.path.join(data_dir, 'results.staramr'), None, False).get_results()
        s = Summary(results, False)
        output = [str(g) for g in s.aggregate_results().values()]
        self.assertEqual(sorted(output), 
                        sorted(["aac(6')-Im\t1", 
                        'ant(6)-Ia\t5', 
                        "aph(2'')-Ib\t1", 
                        "aph(3'')-Ib\t1", 
                        "aph(3')-III\t1", 
                        'aph(6)-Id\t1', 
                        'cepA\t1', 
                        'cfxA\t1', 
                        'cfxA6\t1', 
                        'sul2\t1', 
                        'tet(40)\t2', 
                        'tet(O)\t5', 
                        'tet(Q)\t4', 
                        'tet(X)\t1']))                            