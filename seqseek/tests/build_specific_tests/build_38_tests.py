import os
import fnmatch

from seqseek.chromosome import Chromosome

from seqseek.lib import get_data_directory, BUILD38_CHROMOSOMES, BUILD38

from unittest import TestCase


class TestBuild38(TestCase):

    GRCH38_PATH = os.path.join(get_data_directory(), 'homo_sapiens_GRCh38')

    def test_file_count(self):
        file_count = len(fnmatch.filter(os.listdir(TestBuild38.GRCH38_PATH), '*.fa'))
        self.assertEqual(file_count, 25)

    def test_file_names(self):
        for name in BUILD38_CHROMOSOMES.keys():
            fasta = os.path.join(TestBuild38.GRCH38_PATH,
                                 "chr" + str(name) + ".fa")
            self.assertTrue(os.path.isfile(fasta))

    # all test sequences were extracted from https://genome.ucsc.edu/ using the
    # chromosome browser tool

    def test_chr_start_sequences(self):
        test_str = "N" * 20
        for name in BUILD38_CHROMOSOMES.keys():
            # these chromosomes do not have telomeres
            if name == 'MT'or name == '17':
                continue
            seq = Chromosome(name, assembly=BUILD38).sequence(0, 20)
            self.assertEqual(seq, test_str)

    def test_chr1_sequence(self):
        expected_seq = "ACAGGAAAAAGATAGCATTC"
        seq = Chromosome(1, assembly=BUILD38).sequence(243415701, 243415721)
        self.assertEqual(expected_seq, seq)

    def test_chr2_sequence(self):
        expected_seq = "GCTGGGCCTGAACTGATATC"
        seq = Chromosome(2, assembly=BUILD38).sequence(237518537, 237518557)
        self.assertEqual(expected_seq, seq)

    def test_chr3_sequence(self):
        expected_seq = "GCTGAAGTCATCGATGTGAG"
        seq = Chromosome(3, assembly=BUILD38).sequence(175256410, 175256430)
        self.assertEqual(expected_seq, seq)

    def test_chr4_sequence(self):
        expected_seq = "CTGtttctgaccacagcctc"
        seq = Chromosome(4, assembly=BUILD38).sequence(184624738, 184624758)
        self.assertEqual(expected_seq, seq)

    def test_chr5_sequence(self):
        expected_seq = "CTGTCAATTATCACTGGATC"
        seq = Chromosome(5, assembly=BUILD38).sequence(159073395, 159073415)
        self.assertEqual(expected_seq, seq)

    def test_chr6_sequence(self):
        expected_seq = "GATGCACGCTGCTGTTTTAT"
        seq = Chromosome(6, assembly=BUILD38).sequence(155144605, 155144625)
        self.assertEqual(expected_seq, seq)

    def test_chr7_sequence(self):
        expected_seq = "GAGCTGGTGGGGAGTAACCC"
        seq = Chromosome(7, assembly=BUILD38).sequence(154446213, 154446233)
        self.assertEqual(expected_seq, seq)

    def test_chr8_sequence(self):
        expected_seq = "atcgtggcgtgttctgcagg"
        seq = Chromosome(8, assembly=BUILD38).sequence(132447200, 132447220)
        self.assertEqual(expected_seq, seq)

    def test_chr9_sequence(self):
        expected_seq = "GAACCCTCTCATCGTCAAGG"
        seq = Chromosome(9, assembly=BUILD38).sequence(132410447, 132410467)
        self.assertEqual(expected_seq, seq)

    def test_chr10_sequence(self):
        expected_seq = "TTCAGGTTCCTTTGCAGCTC"
        seq = Chromosome(10, assembly=BUILD38).sequence(122849420, 122849440)
        self.assertEqual(expected_seq, seq)

    def test_chr11_sequence(self):
        expected_seq = "TTTTTAAATGAGTATCCTGG"
        seq = Chromosome(11, assembly=BUILD38).sequence(122850195, 122850215)
        self.assertEqual(expected_seq, seq)

    def test_chr12_sequence(self):
        expected_seq = "CATCCCCAGTTTCCCGCGGG"
        seq = Chromosome(12, assembly=BUILD38).sequence(122850834, 122850854)
        self.assertEqual(expected_seq, seq)

    def test_chr13_sequence(self):
        expected_seq = "CCCCCCGAAAAGGGCAAAGG"
        seq = Chromosome(13, assembly=BUILD38).sequence(113089709, 113089729)
        self.assertEqual(expected_seq, seq)

    def test_chr14_sequence(self):
        expected_seq = "CCCATGTAGTCCAGGTCAGA"
        seq = Chromosome(14, assembly=BUILD38).sequence(100353686, 100353706)
        self.assertEqual(expected_seq, seq)

    def test_chr15_sequence(self):
        expected_seq = "attaaaatcatccaatttcc"
        seq = Chromosome(15, assembly=BUILD38).sequence(86987986, 86988006)
        self.assertEqual(expected_seq, seq)

    def test_chr16_sequence(self):
        expected_seq = "TTTCAAGCCACAGTCGAGGA"
        seq = Chromosome(16, assembly=BUILD38).sequence(83670789, 83670809)
        self.assertEqual(expected_seq, seq)

    def test_chr17_sequence(self):
        expected_seq = "aaacatcatctctaccaaaa"
        seq = Chromosome(17, assembly=BUILD38).sequence(80014178, 80014198)
        self.assertEqual(expected_seq, seq)

    def test_chr18_sequence(self):
        expected_seq = "TGCAAAGAGAAATCCTTgga"
        seq = Chromosome(18, assembly=BUILD38).sequence(67834418, 67834438)
        self.assertEqual(expected_seq, seq)

    def test_chr19_sequence(self):
        expected_seq = "CTGGGCTGCAGAATCGCTGG"
        seq = Chromosome(19, assembly=BUILD38).sequence(45500047, 45500067)
        self.assertEqual(expected_seq, seq)

    def test_chr20_sequence(self):
        expected_seq = "ATGAGATGGACCAAACGCCC"
        seq = Chromosome(20, assembly=BUILD38).sequence(59743106, 59743126)
        self.assertEqual(expected_seq, seq)

    def test_chr21_sequence(self):
        expected_seq = "GGCCCCCCCGGACCACCAGG"
        seq = Chromosome(21, assembly=BUILD38).sequence(45497642, 45497662)
        self.assertEqual(expected_seq, seq)

    def test_chr22_sequence(self):
        expected_seq = "CTTTTCATTAACTGGATAAA"
        seq = Chromosome(22, assembly=BUILD38).sequence(43711474, 43711494)
        self.assertEqual(expected_seq, seq)

    def test_chrX_sequence(self):
        expected_seq = "GGACAACACCtgttaggggc"
        seq = Chromosome("X", assembly=BUILD38).sequence(152811545, 152811565)
        self.assertEqual(expected_seq, seq)

    def test_chrY_sequence(self):
        expected_seq = "CAGACCTTCTGCAGTGCACC"
        seq = Chromosome("Y", assembly=BUILD38).sequence(25325643, 25325663)
        self.assertEqual(expected_seq, seq)

    def test_chrMT_sequence(self):
        expected_seq = "ATTGTACGGTACCATAAATA"
        seq = Chromosome("MT", assembly=BUILD38).sequence(16121, 16141)
        self.assertEqual(expected_seq, seq)
