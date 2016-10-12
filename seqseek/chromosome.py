import os

from .lib import (BUILD37, BUILD38, get_data_directory, sorted_nicely,
                 BUILD37_CHROMOSOMES, BUILD38_CHROMOSOMES)


class MissingDataError(Exception):
    pass


class Chromosome(object):

    ASSEMBLY_CHROMOSOMES = {
        BUILD37: BUILD37_CHROMOSOMES,
        BUILD38: BUILD38_CHROMOSOMES
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
        self.validate_assembly()
        self.chromosome_lengths = self.ASSEMBLY_CHROMOSOMES[self.assembly]
        self.validate_name()
        self.length = self.chromosome_lengths[self.name]

    def validate_assembly(self):
        if self.assembly not in (BUILD37, BUILD38):
            raise ValueError(
            'Sorry, currently the only supported assemblies are {} and {}'.format(
            BUILD37, BUILD38))

    def validate_name(self):
        if self.name not in self.chromosome_lengths.keys():
            raise ValueError("{name} is not a valid chromosome name".format(name=self.name))

    def validate_coordinates(self, start, end, loop=False):
        if loop and self.name != 'MT':
            raise ValueError('Loop may only be specified for the mitochondria.')
        if start < 0 or end < 0:
            raise ValueError("Start and end must be positive integers")
        if end < start:
            raise ValueError("Start position cannot be greater than end position")
        if start > self.length or (end > self.length and not loop):
            raise ValueError('Coordinates out of bounds. Chr {} has {} bases.'.format(
                self.name, self.length))

    @classmethod
    def sorted_chromosome_length_tuples(cls, assembly):
        chromosome_lengths = cls.ASSEMBLY_CHROMOSOMES[assembly]
        return sorted(chromosome_lengths.items(),
                      key=lambda pair:
                          sorted_nicely(
                              chromosome_lengths.keys()).index(pair[0]))

    def filename(self):
       return 'chr{}.fa'.format(self.name)

    def path(self):
        data_dir = get_data_directory()
        return os.path.join(data_dir, self.assembly, self.filename())

    def exists(self):
        return os.path.exists(self.path())

    def header(self):
        header_name = self.name if self.name != 'MT' else 'M'
        return ">chr" + header_name + "\n"

    def read(self, start, length):
        with open(self.path()) as fasta:
            header = fasta.readline()
            fasta.seek(start + len(header))
            return fasta.read(length)

    def sequence(self, start, end, loop=False):
        self.validate_coordinates(start, end, loop=loop)

        if loop and end > self.length:
            # deal with looping around circular mito
            reads = [(start, self.length - start), (0, end - self.length)]
        else:
            reads = [(start, end - start)]

        if not self.exists():
            build = '37' if self.assembly == BUILD37 else '38'
            raise MissingDataError(
                '{} does not exist. Please download on the command line with: '
                'download_build_{}'.format(self.path(), build))

        return ''.join([self.read(*read) for read in reads])
