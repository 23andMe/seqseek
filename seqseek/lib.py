import re
import os


BUILD37 = 'homo_sapiens_GRCh37'
BUILD38 = 'homo_sapiens_GRCh38'
DATA_DIR_VARIABLE = 'SEQSEEK_DATA_DIR'
URI = 'https://s3-us-west-2.amazonaws.com/seqseek/homo_sapiens_GRCh37/'


def get_data_directory():
    default = os.path.expanduser('~/.seqseek')
    storage_dir = os.environ.get(DATA_DIR_VARIABLE, default)
    os.environ[DATA_DIR_VARIABLE] = storage_dir
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    return storage_dir


def sorted_nicely(l):
    """
    Sort the given iterable in the way that humans expect.
    http://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)
