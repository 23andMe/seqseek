import os
import argparse
import requests

from lib import get_data_directory, URI, BUILD37, BUILD38
from chromosome import Chromosome

from tests.build_specific_tests import run_build_test_suite

PROGRAM_TO_ASSEMBLY = {
    'download_build_37': BUILD37,
    'download_build_38': BUILD38
}


def cmd_line():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()

    assembly = PROGRAM_TO_ASSEMBLY[parser.prog]
    verbosity = args.verbose
    data_dir = get_data_directory()

    # Do it
    Downloader(assembly, data_dir, verbosity).download_chromosomes()


class Downloader(object):

    SUPPORTED_ASSEMBLIES = (BUILD37, BUILD38)

    def __init__(self, assembly, data_dir=None, verbose=True):
        self.assembly = assembly
        self.data_dir = data_dir or get_data_directory()
        self.verbose = verbose

        self.validate_assembly()

        self.log('Data directory: {}'.format(self.data_dir))
        self.log('Host: {}'.format(URI))

    def log(self, msg, force=False):
        if self.verbose or force:
            print msg  # TODO: add a log handler

    def validate_assembly(self):
        if self.assembly not in self.SUPPORTED_ASSEMBLIES:
            raise ValueError('%s is not one of the supported assemblies %s'.format(
                self.assembly, self.SUPPORTED_ASSEMBLIES))

    def get_missing_chromosomes(self):
        missing_chromosomes = []

        for name, length in Chromosome.sorted_chromosome_length_tuples(self.assembly):
            chromosome = Chromosome(name, self.assembly)
            filepath = chromosome.path()

            if not chromosome.exists():
                missing_chromosomes.append(name)
            else:
                expected_size = length + len(chromosome.header()) + 1
                size = os.path.getsize(filepath)
                if size != expected_size:
                    self.log('Removing mismatched chromosome %s' % name)
                    missing_chromosomes.append(name)
                    os.remove(filepath)

        return missing_chromosomes

    def download_chromosomes(self):
        to_download = self.get_missing_chromosomes()
        self.log("Downloading {} chromosomes".format(len(to_download)))

        for name in to_download:
            self.download_chromosome(name)
        run_build_test_suite(self.assembly)

    def download_chromosome(self, name):
        chromosome = Chromosome(name, self.assembly)
        path = chromosome.path()
        directory = os.path.dirname(chromosome.path())

        if not os.path.isdir(directory):
            os.makedirs(directory)
            self.log('Created directory {}'.format(directory), True)

        uri = URI + chromosome.filename()

        self.log(
            'Downloading from {} to {}'.format(uri, path), True)

        r = requests.get(uri, stream=True)

        # TODO can we do this in fewer than 3 passes?

        with open(path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)

        with open(path, 'r') as f:
            header = f.readline()
            content = f.read().replace('\n', '')

        with open(path, 'w') as f:
            f.write(header)
            f.write(content)
            f.write('\n')

        self.log('...Complete', True)
