SeqSeek [![Build Status](https://travis-ci.org/23andMe/seqseek.svg?branch=master)](https://travis-ci.org/23andMe/seqseek)
=================
Easy access to Homo sapiens NCBI build 37 and 38 reference sequences.

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
These commands check to see which chromosomes need to be downloaded, fetch any missing 
files, remove newline characters, and run build-specific integrity tests. 
The sequence files are downloaded from our Amazon S3 bucket which contains
FASTA-formatted sequence files obtained from NCBI's nucleotide database 
(e.g. [NC_000001.11](https://www.ncbi.nlm.nih.gov/nuccore/NC_000001.11)).


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
Chromosome(17).sequence(141224, 141244) #=> TTTCCTGAGAGTTCCAGTGA
```
The command above will return a string of 20 nucleotides found between interbase 
positions 141224-141244 on chromosome 17. SeqSeek currently defaults to build
37 to match the coordinates used by the 23andMe website and raw data downloads. 

---

```python
from seqseek import Chromosome, BUILD37, BUILD38
Chromosome(17, assembly=BUILD38).sequence(141224, 141244) #=> ACCTGGTGAGGGGACATGGG
```
You can explicitly specify either build 37 or build 38 using the `BUILD37` and `BUILD38` 
constants and the `assembly` keyword argument. 

---

```python
Chromosome('NC_000017.11'').sequence(141224, 141244)  #=> ACCTGGTGAGGGGACATGGG
```
You can also load a chromosome directly by an accession name instead of specifying both 
the common name and the genome assembly. 


### The Mitochondria 
The mitochondria is a circular piece of DNA and it is sometimes useful to
retrieve sequences that extend beyond the min or max coordinates of the contig
and loop back to the beginning or end. This is mainly useful for pulling
flanking sequences for designing oligonucleotide probes near the extreme 3' and
5' regions of the mitochondria but there may be other applications as well.

We never return sequences that are longer than the length of the contig.
Attempts to load such a sequence raise a TooManyLoops exception

This behavior can be requested by passing `loop=True` when loading the
mitochondria by name. These two invocations return the same sequence: 

```python
Chromosome('MT', loop=True).sequence(-5, 5)         # negative start coordinate  
Chromosome('MT', loop=True).sequence(16564, 16574)  # out of bounds end coordinate
```

SeqSeek uses the revised Cambridge Reference Sequence (rCRS) for the mitochondria on 
both build 37 and 38. If you need access to the out-of-date RSRS sequence for
backward-compatibility then you may load it directly by accession (`NC_001807.4`). 

The rCRS mitochondria sequence contains an 'N' base at position 3106-3107 to
preserve legacy nucleotide numbering. This can be useful for using legacy
coordinates but but is impractical when working with sequences that are
expected to align to observed human mitochondrial sequences. SeqSeek removes this `N`:

```python
Chromosome('MT').sequence(3106, 3107)  # => ''
Chromosome('MT').sequence(3106, 3108)  # => 'T'
```


### Supported chromosome names and accessions 
SeqSeek uses the following common chromosome names: 
`1`, `2`, ..., `22`, `X`, `Y`, and `MT`. 

The full list of supported accessions is as follows:
* NC_000001.10
* NC_000001.11
* NC_000002.11
* NC_000002.12
* NC_000003.11
* NC_000003.12
* NC_000004.11
* NC_000004.12
* NC_000005.9
* NC_000005.10
* NC_000006.11
* NC_000006.12
* NC_000007.13
* NC_000007.14
* NC_000008.10
* NC_000008.11
* NC_000009.11
* NC_000009.12
* NC_000010.10
* NC_000010.11
* NC_000011.9
* NC_000011.10
* NC_000012.11
* NC_000012.12
* NC_000013.10
* NC_000013.11
* NC_000014.8
* NC_000014.9
* NC_000015.9
* NC_000015.10
* NC_000016.9
* NC_000016.10
* NC_000017.10
* NC_000017.11
* NC_000018.9
* NC_000018.10
* NC_000019.9
* NC_000019.10
* NC_000020.10
* NC_000020.11
* NC_000021.8
* NC_000021.9
* NC_000022.10
* NC_000022.11
* NC_000023.10
* NC_000023.11
* NC_000024.10
* NC_000024.9
* NC_001807.4
* NC_012920.1
* NT_113891.2
* NT_167244.1
* NT_167245.1
* NT_167246.1
* NT_167247.1
* NT_167248.1
* NT_167249.1
* NT_167250.1
* NT_167251.1
