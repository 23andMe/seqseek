import os
from unittest import TestCase

from seqseek.exceptions import TooManyLoops
from seqseek.chromosome import Chromosome, MissingDataError
from seqseek.lib import get_data_directory, BUILD37, BUILD37_ACCESSIONS, ACCESSION_LENGTHS, DATA_DIR_VARIABLE


class TestDataDirectory(TestCase):

    TEST_DATA_DIR = os.path.join('seqseek', 'tests', 'test_chromosomes')

    def setUp(self):
        os.environ[DATA_DIR_VARIABLE] = TestChromosome.TEST_DATA_DIR

    def test_get_data_directory(self):
        data_dir = get_data_directory()
        self.assertEqual(TestChromosome.TEST_DATA_DIR, data_dir)

    def test_make_data_directory(self):
        new_dir = os.path.join(TestChromosome.TEST_DATA_DIR, "test")
        self.assertFalse(os.path.isdir(new_dir))
        os.environ[DATA_DIR_VARIABLE] = new_dir
        get_data_directory()
        self.assertTrue(os.path.isdir(new_dir))
        os.rmdir(new_dir)


class TestChromosome(TestCase):

    TEST_DATA_DIR = os.path.join('seqseek', 'tests', 'test_chromosomes')

    def setUp(self):
        mt_accession = BUILD37_ACCESSIONS['MT']
        self._mt_length = ACCESSION_LENGTHS[mt_accession]
        os.environ[DATA_DIR_VARIABLE] = TestChromosome.TEST_DATA_DIR
        ACCESSION_LENGTHS[mt_accession] = 20

    def tearDown(self):
        mt_accession = BUILD37_ACCESSIONS['MT']
        ACCESSION_LENGTHS[mt_accession] = self._mt_length

    def test_invalid_assembly(self):
        with self.assertRaises(ValueError):
            Chromosome('1', 'build_39')

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Chromosome('0', BUILD37)

    def test_no_errors(self):
        Chromosome('1').path()
        Chromosome('1').sorted_chromosome_length_tuples(assembly=BUILD37)
        Chromosome('1').filename()

    def test_chr1_sequences(self):
        expected_seq = 'GGGGCGGGAGGACGGGCCCG'
        seq = Chromosome(1).sequence(0, 20)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(len(seq), 20)
        expected_seq = 'GGGAG'
        seq = Chromosome(1).sequence(5, 10)
        self.assertEqual(seq, expected_seq)

    def test_chrMT_sequence(self):
        expected_seq = 'GATCACAGGTCTTCACCCT'
        seq = Chromosome('MT').sequence(0, 20)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(len(seq), 19)  # the N base was removed
        expected_seq = 'CAGGT'
        seq = Chromosome('MT').sequence(5, 10)
        self.assertEqual(seq, expected_seq)

    def test_rCRS_sequence_retain_N(self):
        expected_seq = 'GATCACAGGTCTNTCACCCT'
        seq = Chromosome('MT', RCRS_N_remove=False).sequence(0, 20)
        self.assertEqual(seq, expected_seq)
        self.assertTrue('N' in seq)  # the N base was *not* removed

    def test_mito_loop_end(self):
        expected_seq = 'CTTCACCCTGATCACAGGT'

        seq = Chromosome('MT', loop=True).sequence(10, 30)
        self.assertEqual(seq, expected_seq)

        seq = Chromosome('MT', loop=True).sequence(-10, 10)
        self.assertEqual(seq, expected_seq)

    def test_others_are_not_circular(self):
        with self.assertRaises(ValueError):
            Chromosome(1, loop=True).sequence(0, 1)

    def test_too_many_loops(self):
        """should never return a sequence longer than the length of the contig"""
        mt_accession = BUILD37_ACCESSIONS['MT']
        mt_length = ACCESSION_LENGTHS[mt_accession]
        Chromosome('MT', loop=True).sequence(0, mt_length)
        with self.assertRaises(TooManyLoops):
            Chromosome('MT', loop=True).sequence(0, mt_length + 1)

        Chromosome('MT', loop=True).sequence(-1, mt_length - 1)
        with self.assertRaises(TooManyLoops):
            Chromosome('MT', loop=True).sequence(-1, mt_length)

    def test_load_by_accession(self):
        # mostly duped from test_chr1_sequences
        expected_seq = 'GGGGCGGGAGGACGGGCCCG'
        seq = Chromosome('NC_000001.10').sequence(0, 20)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(len(seq), 20)
        expected_seq = 'GGGAG'
        seq = Chromosome('NC_000001.10').sequence(5, 10)
        self.assertEqual(seq, expected_seq)


class TestInvalidQueries(TestCase):

    def test_invalid_chromosome_name(self):
        with self.assertRaises(ValueError):
            Chromosome(23).sequence(123456, 123457)

    def test_missing_chromosome(self):
        with self.assertRaises(MissingDataError):
            Chromosome('18').sequence(0, 20)

    def test_invalid_start_position(self):
        with self.assertRaises(ValueError):
            Chromosome(1).sequence(-1, 10)

    def test_invalid_end_position(self):
        with self.assertRaises(ValueError):
            Chromosome(1).sequence(123457, 123456)

    def test_out_of_range_start_position(self):
        with self.assertRaises(ValueError):
            Chromosome(1).sequence(249250623, 249250625)

    def test_out_of_range_end_position(self):
        with self.assertRaises(ValueError):
            Chromosome(1).sequence(249250619, 249250622)
