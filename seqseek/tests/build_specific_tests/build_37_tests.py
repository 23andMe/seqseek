import os

from seqseek.chromosome import Chromosome

from seqseek.lib import get_data_directory, BUILD37_ACCESSIONS, ACCESSION_LENGTHS

from unittest import TestCase


class TestBuild37(TestCase):

    def test_file_names(self):
        for accession in BUILD37_ACCESSIONS.values():
            fasta = os.path.join(get_data_directory(), str(accession) + ".fa")
            self.assertTrue(os.path.isfile(fasta), fasta)

    # all test sequences were extracted from https://genome.ucsc.edu/ using the
    # chromosome browser tool

    def test_chr_start_sequences(self):
        exclude = ('MT', '17' , 'chr6_cox_hap2', 'chr6_apd_hap1', 'chr6_ssto_hap7',
                   'chr6_mcf_hap5', 'chr6_qbl_hap6', 'chr6_mann_hap4', 'chr6_dbb_hap3',
                   'chr17_ctg5_hap1', 'chr4_ctg9_hap1')
        test_str = "N" * 20
        for name in BUILD37_ACCESSIONS.keys():
            # these chromosomes do not have telomeres
            if name in exclude:
                continue
            seq = Chromosome(name).sequence(0, 20)
            self.assertEqual(seq, test_str, name)

    def test_chr1_sequence(self):
        expected_seq = "AATCTAAAAAACTGTCAGAT"
        seq = Chromosome(1).sequence(243400000, 243400020)
        self.assertEqual(expected_seq.upper(), seq)

    def test_chr2_sequence(self):
        expected_seq = "tgtccacgcgcggatgtcgt"
        seq = Chromosome(2).sequence(237513040, 237513060)
        self.assertEqual(expected_seq.upper(), seq)

    def test_chr3_sequence(self):
        expected_seq = "ctctttcgcccaggctggag"
        seq = Chromosome(3).sequence(190352536, 190352556)
        self.assertEqual(expected_seq.upper(), seq)

    def test_chr4_sequence(self):
        expected_seq = "ttggagccaaggtctcactc"
        seq = Chromosome(4).sequence(184622015, 184622035)
        self.assertEqual(expected_seq.upper(), seq)

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
        self.assertEqual(expected_seq.upper(), seq)

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
        expected_seq = "ATTGTACGGTACCATAAATA"
        seq = Chromosome("MT").sequence(16121, 16141)
        self.assertEqual(expected_seq, seq)

    def test_chr6_cox_hap2(self):
        accession = BUILD37_ACCESSIONS['chr6_cox_hap2']
        max_length = ACCESSION_LENGTHS[accession]

        expected_seq = "GATCCTGAGTGGGTGAGTGG"
        seq = Chromosome("chr6_cox_hap2").sequence(3065395, 3065415)
        self.assertEqual(expected_seq, seq)

        expected_seq = "TATTCTTGCCAATAT"
        seq = Chromosome("chr6_cox_hap2").sequence(200, 215).upper()
        self.assertEqual(expected_seq, seq)

        expected_seq = "TCTGGCCTGGGAGTC"
        seq = Chromosome("chr6_cox_hap2").sequence(0, 15).upper()
        self.assertEqual(expected_seq, seq)

        expected = "tc"
        seq = Chromosome('chr6_cox_hap2').sequence(4795369, max_length)
        self.assertEqual(expected.upper(), seq)

    def test_chr6_apd_hap1(self):
        accession = BUILD37_ACCESSIONS['chr6_apd_hap1']
        max_length = ACCESSION_LENGTHS[accession]

        expected = "GAATTCAGCTCGCCGACGGC"
        seq = Chromosome('chr6_apd_hap1').sequence(0, 20)
        self.assertEqual(expected, seq)

        expected = "ACAATTAGAAATACTAGGAG"
        seq = Chromosome('chr6_apd_hap1').sequence(3000, 3020)
        self.assertEqual(expected, seq)

        expected = "cacT"
        seq = Chromosome('chr6_apd_hap1').sequence(max_length - 4, max_length)
        self.assertEqual(expected.upper(), seq)

    def test_chr6_ssto_hap7(self):
        accession = BUILD37_ACCESSIONS['chr6_ssto_hap7']
        max_length = ACCESSION_LENGTHS[accession]

        expected = "GGCCAGGTTTTGTGAATTCT"
        seq = Chromosome('chr6_ssto_hap7').sequence(3000, 3020)
        self.assertEqual(expected.upper(), seq)

        expected = "ggcc"
        seq = Chromosome('chr6_ssto_hap7').sequence(max_length - 4, max_length)
        self.assertEqual(expected.upper(), seq)

    def test_chr6_mcf_hap5(self):
        expected = "ACAATTAGAAATACTAGGAG"
        seq = Chromosome('chr6_mcf_hap5').sequence(3000, 3020)
        self.assertEqual(expected, seq)

    def test_chr6_qbl_hap6(self):
        accession = BUILD37_ACCESSIONS['chr6_qbl_hap6']
        max_length = ACCESSION_LENGTHS[accession]

        expected = "ACAATTAGAAATACTAGGAG"
        seq = Chromosome('chr6_qbl_hap6').sequence(3000, 3020)
        self.assertEqual(expected, seq)

        expected = "ggcc"
        seq = Chromosome('chr6_qbl_hap6').sequence(max_length - 4, max_length)
        self.assertEqual(expected.upper(), seq)

    def test_chr6_mann_hap4(self):
        expected = "ACAATTAGAAATACTAGGAG"
        seq = Chromosome('chr6_mann_hap4').sequence(3000, 3020)
        self.assertEqual(expected, seq)

    def test_chr6_dbb_hap3(self):
        expected = "ACAATTAGAAATACTAGGAG"
        seq = Chromosome('chr6_dbb_hap3').sequence(3000, 3020)
        self.assertEqual(expected, seq)

    def test_chr17_ctg5_hap1(self):
        expected = "TTTTGGCTACAATAATTCTT"
        seq = Chromosome('chr17_ctg5_hap1').sequence(3000, 3020)
        self.assertEqual(expected, seq)

    def test_looped_mito(self):
        mito_accession = BUILD37_ACCESSIONS['MT']
        mito_length = ACCESSION_LENGTHS[mito_accession]
        expected = 'CATCACGATGGATCACAGGT'

        seq = Chromosome('MT', loop=True).sequence(mito_length - 10, mito_length + 10)
        self.assertEqual(expected, seq)

        seq = Chromosome('MT', loop=True).sequence(-10, 10)
        self.assertEqual(expected, seq)

    def test_mito_N(self):
        """
        From mitomap:
            *3107del is maintained in this revised sequence with the gap
            represented by an 'N'. THIS ALLOWS HISTORICAL NUCLEOTIDE NUMBERING TO
            BE MAINTAINED.

        We remove this 'N' base since it is only present to preserve numbering and is
        not actually part of the observed sequence.
        """
        self.assertEqual('', Chromosome('MT').sequence(3106, 3107))
