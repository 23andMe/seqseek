import os
import argparse
import requests

from lib import get_data_directory, URI37, URI38, BUILD37, BUILD38
from chromosome import Chromosome

from tests.build_specific_tests import run_build_test_suite

SUPPORTED_URIS = {
    'download_build_37': URI37,
    'download_build_38': URI38
}


def cmd_line():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('--uri', dest='uri', default=URI37)
    args = parser.parse_args()
    if parser.prog in SUPPORTED_URIS.keys():
        uri = SUPPORTED_URIS[parser.prog]
    else:
        uri = args.uri
    verbosity = args.verbose
    data_dir = get_data_directory()

    # Do it
    Downloader(uri, data_dir, verbosity).download_chromosomes()


class Downloader(object):

    SUPPORTED_ASSEMBLIES = {
        URI37: BUILD37,
        URI38: BUILD38
    }

    def __init__(self, uri, data_dir, verbose):
        self.uri = uri
        self.data_dir = data_dir
        self.verbose = verbose
        self.log('Data directory: {}'.format(data_dir))
        self.log('Host: {}'.format(self.uri))
        self.assembly = Downloader.SUPPORTED_ASSEMBLIES[self.uri]

    def log(self, msg, force=False):
        if self.verbose or force:
            print msg
        # TODO: add a log handler

    def get_missing_chromosomes(self):
        missing_chromosomes = []

        for name, length in Chromosome.sorted_chromosome_length_tuples(self.assembly):
            chromosome = Chromosome(name, self.assembly)
            filepath = chromosome.path()

            if not os.path.isfile(filepath):
                missing_chromosomes.append(name)
            else:
                expected_size = length + len(chromosome.header()) + 1
                size = os.path.getsize(filepath)
                if size != expected_size:
                    missing_chromosomes.append(name)
                    os.remove(filepath)

        return missing_chromosomes

    def download_chromosomes(self):
        to_download = self.get_missing_chromosomes()
        self.log("Downloading {} chromosomes".format(len(to_download)))

        for name in to_download:
            chromosome = Chromosome(name, self.assembly)
            self.log(chromosome.path())
            path = chromosome.path()
            directory = os.path.dirname(chromosome.path())
            if not os.path.isdir(directory):
                os.makedirs(directory)
                self.log('Created directory {}'.format(directory), True)

            self.log(
                'Downloading {}{} to {}'.format(self.uri, chromosome.filename(), path),
                 force=True)

            r = requests.get(self.uri + chromosome.filename(), stream=True)
            with open(path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)
            self.log('Complete', True)

        run_build_test_suite(self.assembly)
