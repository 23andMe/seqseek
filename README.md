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

TODO: GET THIS WORKING TODAY. Manual works for now.

$ pip install seqseek
$ download_build_37  -v
```

### Manual
1. Download seqseek from: https://github.com/23andMe/seqseek/archive/master.zip
2. Unzip somewhere temporary
3. Run `python setup.py install` (may have to prepend `sudo`)
4. Install data: `download_build_37  -v`
