import os
import fnmatch

from seqseek.chromosome import Chromosome

from seqseek.lib import get_data_directory, BUILD37_CHROMOSOMES, BUILD37

from unittest import TestCase

# pragma: no cover
class TestBuild37(TestCase):

    GRCH37_PATH = os.path.join(get_data_directory(), 'homo_sapiens_GRCh37')

    def test_file_count(self):
        file_count = len(fnmatch.filter(os.listdir(TestBuild37.GRCH37_PATH), '*.fa'))
        self.assertEqual(file_count, 25)

    def test_file_names(self):
        for name in BUILD37_CHROMOSOMES.keys():
            fasta = os.path.join(TestBuild37.GRCH37_PATH,
                                 "chr" + str(name) + ".fa")
            self.assertTrue(os.path.isfile(fasta))

    # all test sequences were extracted from https://genome.ucsc.edu/ using the
    # chromosome browser tool

    def test_chr_start_sequences(self):
        test_str = "N" * 20
        for name in BUILD37_CHROMOSOMES.keys():
            # these chromosomes do not have telomeres
            if name == 'MT'or name == '17':
                continue
            seq = Chromosome(name).sequence(0, 20)
            self.assertEqual(seq, test_str)

    def test_chr1_sequence(self):
        expected_seq = "AATCTAAAAAACTGTCAGAT"
        seq = Chromosome(1).sequence(243400000, 243400020)
        self.assertEqual(expected_seq, seq)

    def test_chr2_sequence(self):
        expected_seq = "tgtccacgcgcggatgtcgt"
        seq = Chromosome(2).sequence(237513040, 237513060)
        self.assertEqual(expected_seq, seq)

    def test_chr3_sequence(self):
        expected_seq = "ctctttcgcccaggctggag"
        seq = Chromosome(3).sequence(190352536, 190352556)
        self.assertEqual(expected_seq, seq)

    def test_chr4_sequence(self):
        expected_seq = "ttggagccaaggtctcactc"
        seq = Chromosome(4).sequence(184622015, 184622035)
        self.assertEqual(expected_seq, seq)

    def test_chr5_sequence(self):
        expected_seq = "CTTTACTCCACTCATATTCT"
        seq = Chromosome(5).sequence(158879589, 158879609)
        self.assertEqual(expected_seq, seq)

    def test_chr6_sequence(self):
        expected_seq = "AGGTGGTAGCCCAGTGGTGC"
        seq = Chromosome(6).sequence(158882594, 158882614)
        self.assertEqual(expected_seq, seq)

    def test_chr7_sequence(self):
        expected_seq = "CTTGCTCTCATCCTCCGGGT"
        seq = Chromosome(7).sequence(158896447, 158896467)
        self.assertEqual(expected_seq, seq)

    def test_chr8_sequence(self):
        expected_seq = "CTGTCTCCACTGCAGGGCTC"
        seq = Chromosome(8).sequence(139508913, 139508933)
        self.assertEqual(expected_seq, seq)

    def test_chr9_sequence(self):
        expected_seq = "GAGGAGAACATTTGCCTGCA"
        seq = Chromosome(9).sequence(140705912, 140705932)
        self.assertEqual(expected_seq, seq)

    def test_chr10_sequence(self):
        expected_seq = "TCTGCAGGGGGCGGAGGAAA"
        seq = Chromosome(10).sequence(121086020, 121086040)
        self.assertEqual(expected_seq, seq)

    def test_chr11_sequence(self):
        expected_seq = "CTGAGGGTGGCGCTCTCCCC"
        seq = Chromosome(11).sequence(132812820, 132812840)
        self.assertEqual(expected_seq, seq)

    def test_chr12_sequence(self):
        expected_seq = "CCTCATGCCCAGTTCTACGT"
        seq = Chromosome(12).sequence(132824462, 132824482)
        self.assertEqual(expected_seq, seq)

    def test_chr13_sequence(self):
        expected_seq = "GAAAAGAATTCAAAGAACAC"
        seq = Chromosome(13).sequence(113086756, 113086776)
        self.assertEqual(expected_seq, seq)

    def test_chr14_sequence(self):
        expected_seq = "GCAACGGGGTGGTCATCCAC"
        seq = Chromosome(14).sequence(105204712, 105204732)
        self.assertEqual(expected_seq, seq)

    def test_chr15_sequence(self):
        expected_seq = "ttcaatcactgatacccttt"
        seq = Chromosome(15).sequence(99921491, 99921511)
        self.assertEqual(expected_seq, seq)

    def test_chr16_sequence(self):
        expected_seq = "CTTTCAGCACAGGGCTGTGA"
        seq = Chromosome(16).sequence(89862313, 89862333)
        self.assertEqual(expected_seq, seq)

    def test_chr17_sequence(self):
        expected_seq = "TGGAGCTGGAGCCACAGGTC"
        seq = Chromosome(17).sequence(80014178, 80014198)
        self.assertEqual(expected_seq, seq)

    def test_chr18_sequence(self):
        expected_seq = "CGAACACTTCGTTGTCCTCT"
        seq = Chromosome(18).sequence(74778253, 74778273)
        self.assertEqual(expected_seq, seq)

    def test_chr19_sequence(self):
        expected_seq = "GGCTGGTTAAACTCGGGGTC"
        seq = Chromosome(19).sequence(55798374, 55798394)
        self.assertEqual(expected_seq, seq)

    def test_chr20_sequence(self):
        expected_seq = "CTGCCCAAGTGCTCCTGGAG"
        seq = Chromosome(20).sequence(55803284, 55803304)
        self.assertEqual(expected_seq, seq)

    def test_chr21_sequence(self):
        expected_seq = "GGCTGGTGTGGCACATGATG"
        seq = Chromosome(21).sequence(46074515, 46074535)
        self.assertEqual(expected_seq, seq)

    def test_chr22_sequence(self):
        expected_seq = "AGACGCCGCCCCTGTTCATG"
        seq = Chromosome(22).sequence(50552076, 50552096)
        self.assertEqual(expected_seq, seq)

    def test_chrX_sequence(self):
        expected_seq = "GCAAGCAGCAGGATGGGGCC"
        seq = Chromosome("X").sequence(152811545, 152811565)
        self.assertEqual(expected_seq, seq)

    def test_chrY_sequence(self):
        expected_seq = "CTGAACGTGCTGAGTTACAG"
        seq = Chromosome("Y").sequence(25325643, 25325663)
        self.assertEqual(expected_seq, seq)

    def test_chrMT_sequence(self):
        expected_seq = "TATTGTACGGTACCATAAAT"
        seq = Chromosome("MT").sequence(16121, 16141)
        self.assertEqual(expected_seq, seq)
