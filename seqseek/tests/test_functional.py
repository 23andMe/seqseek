from seqseek.chromosome import Chromosome

def test_no_errors():
    Chromosome('1').path()
    Chromosome('1').sorted_chromosome_length_tuples()
    Chromosome('1').filename()

