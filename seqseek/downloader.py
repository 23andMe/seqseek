#!/usr/bin/env python

import argparse
import os
import subprocess

from ftplib import FTP

from ttam.seqseek import Chromosome
from ttam.seqseq.lib import get_data_directory


FASTA_PATH = os.path.join("ttam", "seqseek", "fastas")
HOSTNAME = 'ftp.ensembl.org'
FTPDIR = '/pub/grch37/release-83/fasta/homo_sapiens/dna'


parser = argparse.ArgumentParser(description='')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true')
parser.add_argument('--host', dest='host', default=HOSTNAME)
parser.add_argument('--path', dest='path', default=FTPDIR)


class Downloader(object):

    def __init__(self, host, path, data_dir, verbose):
        self.host = host
        self.path = path
        self.verbose = verbose
        self.data_dir = data_dir
        self.log('FTP: host is {}'.format(self.host))
        self.log('FTP: writing to directory {}'.format(data_dir))

    def log(self, msg, force=False):
        if self.verbose or force:
            print msg
        # TODO: add a log handler

    def prep_fastas(self):
        subprocess.call("./prep_fastas.sh", shell=True)

    def get_missing_chromosomes(self):
        missing_chromosomes = []

        for chrom, length in Chromosome.sorted_chromosome_length_tuples:
            filepath = Chromosome(chrom).path()

            if not os.path.isfile(filepath):
                missing_chromosomes.append(chrom)
                continue

            expected_size = length + len('>chr' + chrom + "\n") + 1
            size = os.path.getsize(filepath)
            if size != expected_size:
                missing_chromosomes.append(chrom)
                os.remove(filepath)

        return missing_chromosomes

    def download_chromosomes(self):
        to_download = self.get_missing_chromosomes()
        self.log("FTP: need to download {} chromosomes".format(len(to_download)))

        if to_download:
            ftp = FTP(HOSTNAME)
            self.log("FTP: establishing connection with {}".format(HOSTNAME))

            ftp.login()
            self.log("FTP: connection established")

            ftp.cwd(FTPDIR)
            self.log("FTP: current directory is {}".format(ftp.pwd()))

            for name in to_download:
                chromosome = Chromosome(name)
                filename = chromosome.filename()
                path = os.path.join(self.data_dir, 'tmp_ensembl' + chromosome.filename)
                handle = open(path, 'wb')

                self.log("FTP: downloading {} to {}".format(filename, path))
                ftp.retrbinary('RETR %s' % filename, handle.write)
                self.log("FTP: {} COMPLETE".format(filename), True)

            self.log("FTP: closing connection")
            ftp.quit()
            self.log("FTP: connection closed")

            self.log("FASTA: post-processing files")
            self.prep_fastas()
            self.log("FASTA: post-processing complete")


if __name__ == '__main__':
    args = parser.parse_args()
    host = args.host
    path = args.path
    verbose = args.verbose
    data_dir = get_data_directory()
    Downloader(host, path, data_dir, verbose).download_chromosomes()
