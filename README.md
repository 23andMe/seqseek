SeqSeek
=================
Easy access to Homo sapiens NCBI Build 37 and 38 reference sequences

This package calls open(file).seek(range) on FASTA files of ASCII to provide
ranges of sequence strings. It is exactly as fast as your disk, for better or worse.

Requirements
------------
* Python 2.7+

Install
-------
### pip
```bash
$ pip install seqseek
```

### Download Utilities
```bash
$ download_build_37 -v
$ download_build_38 -v
```
These commands check to see which chromosomes you need to download for the
specified build and initiates a download from our Amazon S3 bucket. Use
the `-v` flag to speficty the verbosity. Use the `-uri` command to specify an
alternative download site. The commands automatically run build-specific tests
to ensure the integrity of the download.

### Test Utilities
```bash
$ test_build_37
$ test_build_38
```
These commands run build specific tests to ensure the chromosome files have been
downloaded correctly. These tests extract sequences from each chromosome file and
compare the extracted sequence with sequences pulled from https://genome.ucsc.edu.
