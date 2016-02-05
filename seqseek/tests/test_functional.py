import os
import fnmatch

from shutil import copyfile, rmtree

from seqseek.chromosome import Chromosome, MissingDataError

from ..lib import get_data_directory, BUILD37, URI37

from unittest import TestCase


class TestDataDirectory(TestCase):

    TEST_DATA_DIR = os.path.join('seqseek', 'tests', 'test_chromosomes')

    def setUp(self):
        os.environ['DATA_DIR_VARIABLE'] = TestChromosome.TEST_DATA_DIR

    def test_get_data_directory(self):
        data_dir = get_data_directory()
        self.assertEqual(TestChromosome.TEST_DATA_DIR, data_dir)

    def test_make_data_directory(self):
        new_dir = os.path.join(TestChromosome.TEST_DATA_DIR, "test")
        self.assertFalse(os.path.isdir(new_dir))
        os.environ['DATA_DIR_VARIABLE'] = new_dir
        get_data_directory()
        self.assertTrue(os.path.isdir(new_dir))
        os.rmdir(new_dir)


class TestChromosome(TestCase):

    TEST_DATA_DIR = os.path.join('seqseek', 'tests', 'test_chromosomes')

    def setUp(self):
        os.environ['DATA_DIR_VARIABLE'] = TestChromosome.TEST_DATA_DIR

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
        expected_seq = 'GATCACAGGTCTATCACCCT'
        seq = Chromosome('MT').sequence(0, 20)
        self.assertEqual(seq, expected_seq)
        self.assertEqual(len(seq), 20)
        expected_seq = 'CAGGT'
        seq = Chromosome('MT').sequence(5, 10)
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
