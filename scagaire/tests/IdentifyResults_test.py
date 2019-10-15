import unittest
import os
import shutil
from scagaire.IdentifyResults  import IdentifyResults

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','identify_results')

class TestIdentifyResults(unittest.TestCase):
    
    def test_abricate_results(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.abricate'), None, False).get_results()
    
        self.assertEqual(str(a[0]), "assembly.fasta	contig_10165	108800	110741	+	tet(M)	1-1920/1920	========/======	36/40	99.53	97.18	ncbi	NG_048232.1	tetracycline resistance ribosomal protection protein Tet(M)	TETRACYCLINE")
        
    def test_abricate_results_specific(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.abricate'), 'abricate', False).get_results()
    
        self.assertEqual(str(a[0]), "assembly.fasta	contig_10165	108800	110741	+	tet(M)	1-1920/1920	========/======	36/40	99.53	97.18	ncbi	NG_048232.1	tetracycline resistance ribosomal protection protein Tet(M)	TETRACYCLINE")
           
    def test_staramr_results(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.staramr'), None, False).get_results()
        self.assertEqual(len(a), 1)
        self.assertEqual(str(a[0]), "assembly	aac(6')-Im	gentamicin	98.16	100.93	542/537	contig_8118	24866	24328	AF337947")
        
    def test_staramr_results_specific(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.staramr'), 'staramr', False).get_results()
        self.assertEqual(len(a), 1)
        self.assertEqual(str(a[0]), "assembly	aac(6')-Im	gentamicin	98.16	100.93	542/537	contig_8118	24866	24328	AF337947")
        
        
    def test_rgi_results(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.rgi'), None, False).get_results()
        self.assertEqual(len(a), 1)
        self.assertEqual(str(a[0]), "contig_3632_125 # 73122 # 73460 # -1 # ID=1_125;partial=00;start_type=GTG;rbs_motif=None;rbs_spacer=None;gc_cont=0.584	contig_3632_125 	73122	73460	-	Strict	500	210.305	APH(6)-Id	98.06	3002660	protein homolog model	n/a	n/a	aminoglycoside antibiotic	antibiotic inactivation	APH(6)	GTGGGCTACATGGCGATCTGCATCATGAAAAACATCATGTTCTCCAGTCGCGGCTGGCTGGTGATAGATCCCGTCGGTCTGGTCGGTGAAGTGGGCTTTGGCGCCGCCAATATGTTCTACGATCCGGCTGACAGAGACGACCTTTGTCTCGATCCTAGACGCATTGCACAGATGGCGGACGCATTCTCTCGTGCGCTGGACGTCGATCCGCGTCGCCTGCTCGACCAGGCGTACGCTTATGGGTGCCTTTCCGCAGCTTGGAACGCGGATGGAGAAGAGGAGCAACGCGATCTAGCTATCGCGGCCGCGATCAAGCAGGTGCGACAGACGTCATACTAG	MGYMAICIMKNIMFSSRGWLVIDPVGLVGEVGFGAANMFYDPADRDDLCLDPRRIAQMADAFSRALDVDPRRLLDQAYAYGCLSAAWNADGEEEQRDLAIAAAIKQVRQTSY	MFMPPVFPAHWHVSQPVLIADTFSSLVWKVSLPDGTPAIVKGLKPIEDIADELRGADYLVWRNGRGAVRLLGRENNLMLLEYAGERMLSHIVAEHGDYQATEIAAELMAKLYAASEEPLPSALLPIRDRFAALFQRARDDQNAGCQTDYVHAAIIADQMMSNASELRGLHGDLHHENIMFSSRGWLVIDPVGLVGEVGFGAANMFYDPADRDDLCLDPRRIAQMADAFSRALDVDPRRLLDQAYAYGCLSAAWNADGEQEQRDLAIAAAIKQVRQTSY	40.29	gnl|BL_ORD_ID|972|hsp_num:0	1031	True	loose hit with at least 95 percent identity pushed strict")

    def test_rgi_results_specific(self):
        a = IdentifyResults(os.path.join(data_dir, 'results.rgi'), 'rgi', False).get_results()
        self.assertEqual(len(a), 1)
        self.assertEqual(str(a[0]), "contig_3632_125 # 73122 # 73460 # -1 # ID=1_125;partial=00;start_type=GTG;rbs_motif=None;rbs_spacer=None;gc_cont=0.584	contig_3632_125 	73122	73460	-	Strict	500	210.305	APH(6)-Id	98.06	3002660	protein homolog model	n/a	n/a	aminoglycoside antibiotic	antibiotic inactivation	APH(6)	GTGGGCTACATGGCGATCTGCATCATGAAAAACATCATGTTCTCCAGTCGCGGCTGGCTGGTGATAGATCCCGTCGGTCTGGTCGGTGAAGTGGGCTTTGGCGCCGCCAATATGTTCTACGATCCGGCTGACAGAGACGACCTTTGTCTCGATCCTAGACGCATTGCACAGATGGCGGACGCATTCTCTCGTGCGCTGGACGTCGATCCGCGTCGCCTGCTCGACCAGGCGTACGCTTATGGGTGCCTTTCCGCAGCTTGGAACGCGGATGGAGAAGAGGAGCAACGCGATCTAGCTATCGCGGCCGCGATCAAGCAGGTGCGACAGACGTCATACTAG	MGYMAICIMKNIMFSSRGWLVIDPVGLVGEVGFGAANMFYDPADRDDLCLDPRRIAQMADAFSRALDVDPRRLLDQAYAYGCLSAAWNADGEEEQRDLAIAAAIKQVRQTSY	MFMPPVFPAHWHVSQPVLIADTFSSLVWKVSLPDGTPAIVKGLKPIEDIADELRGADYLVWRNGRGAVRLLGRENNLMLLEYAGERMLSHIVAEHGDYQATEIAAELMAKLYAASEEPLPSALLPIRDRFAALFQRARDDQNAGCQTDYVHAAIIADQMMSNASELRGLHGDLHHENIMFSSRGWLVIDPVGLVGEVGFGAANMFYDPADRDDLCLDPRRIAQMADAFSRALDVDPRRLLDQAYAYGCLSAAWNADGEQEQRDLAIAAAIKQVRQTSY	40.29	gnl|BL_ORD_ID|972|hsp_num:0	1031	True	loose hit with at least 95 percent identity pushed strict")

