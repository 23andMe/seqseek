import os

from .lib import BUILD37, BUILD38, get_data_directory, sorted_nicely


class MissingDataError(Exception):
    pass


class Chromosome(object):

    CHROMOSOME_LENGTHS = {
        '1': 249250621,
        '2': 243199373,
        '3': 198022430,
        '4': 191154276,
        '5': 180915260,
        '6': 171115067,
        '7': 159138663,
        '8': 146364022,
        '9': 141213431,
        '10': 135534747,
        '11': 135006516,
        '12': 133851895,
        '13': 115169878,
        '14': 107349540,
        '15': 102531392,
        '16': 90354753,
        '17': 81195210,
        '18': 78077248,
        '19': 59128983,
        '20': 63025520,
        '21': 48129895,
        '22': 51304566,
        'X':  155270560,
        'Y':  59373566,
        'MT': 16571
    }

    def __init__(self, chromosome_name, assembly=BUILD37):
        """
        Usage:

                Chromosome('1').sequence(0, 100)
                returns the first 100 nucleotides of chromosome 1

        The default assembly is Homo_sapiens.GRCh37
        You may also use Build 38::

                from seqseek import BUILD38
                Chromosome('1', BUILD38).sequence(0, 100)
        """
        self.name = str(chromosome_name)
        self.assembly = assembly
        self.validate()
        self.length = self.CHROMOSOME_LENGTHS[self.name]

    def validate(self):
        if self.name not in self.CHROMOSOME_LENGTHS:
            raise ValueError("{name} is not a valid chromosome name!".format(self.name))
        if self.assembly not in (BUILD37, BUILD37):
            raise ValueError(
                'Sorry, currently the only supported assemblies are {} and {}'.format(
                    BUILD37, BUILD38))

    def validate_coordinates(self, start, end):
        if start < 0 or end < 0:
            raise ValueError("Start and end must be positive integers")
        if end < start:
            raise ValueError("Start position cannot be greater than end position")
        if start > self.length or end > self.length:
            raise ValueError('Coordinates out of bounds. Chr {} has {} bases.'.format(
                self.name, self.length))

    @classmethod
    def sorted_chromosome_length_tuples(cls):
        return sorted(cls.CHROMOSOME_LENGTHS.items(),
                      key=lambda pair:
                          sorted_nicely(
                              Chromosome.CHROMOSOME_LENGTHS.keys()).index(pair[0]))

    def filename(self):
       return 'chr{}.fa'.format(self.name)

    def path(self):
        data_dir = get_data_directory()
        return os.path.join(data_dir, BUILD37, self.filename())

    def exists(self):
        return os.path.exists(self.path())

    def sequence(self, start, end):
        self.validate_coordinates(start, end)
        seq_length = end - start

        if not self.exists():
            raise MissingDataError(
                '{} does not exist. Please download on the command line with: '
                'seqseek download {}'.format(self.path(), self.assembly))
        with open(self.filename()) as fasta:
            # each file has a header like ">chr15" followed by a newline
            fasta.seek(start + len(">" + self.filename() + "\n"))
            return fasta.read(seq_length)
