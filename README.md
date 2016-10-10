SeqSeek [![Build Status](https://travis-ci.org/23andMe/seqseek.svg?branch=master)](https://travis-ci.org/23andMe/seqseek)
=================
Easy access to Homo sapiens NCBI Build 37 and 38 reference sequences.

This package calls open(file).seek(range) on FASTA files of ASCII characters to provide
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
$ download_build_37 
$ download_build_38 
```
These commands check to see which chromosomes need to be downloaded for the
specified build and initiate a download from our Amazon S3 bucket. Use
the `-v` flag to turn verbosity on/off. Use the `-uri` flag to specify an
alternative download site. These commands automatically run build-specific tests
to ensure the integrity of the download once it is finished.

The chromosome files in this package were downloaded from
http://hgdownload.cse.ucsc.edu/goldenpath/hg19/chromosomes/. The files have been
modified - all newline characters have been removed from the fasta files to make
retrieving sequences more simple.

In these files, lower-case letters are used to represent repeating sequences. N's
are used to represent any nucleotide (A, T, C, or G). With the exception of 
chromosome MT (and chromosome 17 in Build 37), all of the chromosome files begin 
and end with a long sequence of N's.


### Test Utilities
```bash
$ test_build_37
$ test_build_38
```
These commands run build specific tests to ensure the chromosome files have been
downloaded correctly. These tests read sequences from each chromosome file and
compare the extracted sequence with sequences pulled from https://genome.ucsc.edu.


### Using the seqseek package
```python
from seqseek import Chromosome
```
Import the chromosome class from the seqseek package.

```python
Chromosome(17).sequence(start=141224, end=141244) #=> TTTCCTGAGAGTTCCAGTGA
```
The command above will return a string of 20 nucleotides from chromosome 17.

```python
from seqseek import Chromosome, BUILD38
Chromosome(17, assembly=BUILD38).sequence(start=141224, end=141244) #=> ACCTGGTGAGGGGACATGGG
```
Build 37 is the default. You can specify another build with the assembly option,
as shown above. 
