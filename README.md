SeqSeek (sequence seek) 
=================
Easy access to Homo sapiens NCBI Build 37 and 38 reference sequences

This package calls open(file).seek(range) on FASTA files of ASCII to provide 
ranges of sequence strings. It is exactly as fast as your disk, for better or worse. 


[![Build Status](https://travis-ci.org/23andMe/seqseek.svg?branch=master)](https://travis-ci.org/23andMe/seqseek)
[![PyPI](https://img.shields.io/pypi/v/seqseek.svg)](https://pypi.python.org/pypi/seqseek)

Requirements
------------
* Python 2.7+
* Python 3.4+ (Only tested on 3.4, may work on older versions)

Install
-------
### pip
```bash
$ pip install seqseek
```

### Manual
1. Download seqseek from: https://github.com/23andMe/seqseek/archive/master.zip
2. Unzip somewhere temporary
3. Run `python setup.py install` (may have to prepend `sudo`)
