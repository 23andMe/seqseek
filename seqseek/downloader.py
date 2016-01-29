import os
import argparse
import subprocess
import requests
from lib import get_data_directory, URI
from chromosome import Chromosome


def cmd_line():
    print 'begin cmd line'
    parser = argparse.ArgumentParser(description='')
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('--uri', dest='uri', default=URI)

    args = parser.parse_args()
    uri = args.uri
    verbosity = args.verbose
    data_dir = get_data_directory()

    # Do it
    Downloader(uri, data_dir, verbosity).download_chromosomes()


class Downloader(object):

    def __init__(self, uri, data_dir, verbose):
        self.uri = uri
        self.data_dir = data_dir
        self.verbose = verbose
        self.log('Data directory: {}'.format(data_dir))
        self.log('Host: {}'.format(self.uri))

    def log(self, msg, force=False):
        if self.verbose or force:
            print msg
        # TODO: add a log handler

    def get_missing_chromosomes(self):
        missing_chromosomes = []

        for name, length in Chromosome.sorted_chromosome_length_tuples():
            chromosome = Chromosome(name)
            filepath = chromosome.path()

            if not os.path.isfile(filepath):
                missing_chromosomes.append(name)
            else:
                expected_size = length + len('>chr' + name + "\n") + 1
                size = os.path.getsize(filepath)
                if size != expected_size:
                    missing_chromosomes.append(name)
                    os.remove(filepath)

        return missing_chromosomes

    def download_chromosomes(self):
        to_download = self.get_missing_chromosomes()
        self.log("Downloading {} chromosomes".format(len(to_download)))

        for name in to_download:
            chromosome = Chromosome(name)
            filename = chromosome.filename()
            path = chromosome.path()
            directory = os.path.dirname(chromosome.path())
            if not os.path.isdir(directory):
                os.makedirs(directory)
                self.log('created directory {}'.format(directory))
            fd = open(path, 'wb')

            self.log('Downloading {} to {}'.format(self.uri + chromosome.filename(), path))
            r = requests.get(self.uri + chromosome.filename(), stream=True)
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)
            self.log('Complete')
