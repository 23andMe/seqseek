import re
import os


BUILD37 = 'homo_sapiens_GRCh37'
BUILD38 = 'homo_sapiens_GRCh38'

DEFAULT_DATA_DIR = '~/.seqseek'
DATA_DIR_VARIABLE = 'SEQSEEK_DATA_DIR'

URI37 = 'https://s3-us-west-2.amazonaws.com/seqseek/homo_sapiens_GRCh37/'
URI38 = 'https://s3-us-west-2.amazonaws.com/seqseek/homo_sapiens_GRCh38/'

# chromosome names and lengths for build 37
BUILD37_CHROMOSOMES = {
    '1': 249250621,
    '2': 243199373,
    '3': 198022430,
    '4': 191154276,
    '5': 180915260,
    '6': 171115067,
    '7': 159138663,
    '8': 146364022,
    '9': 141213431,
    '10': 135534747,
    '11': 135006516,
    '12': 133851895,
    '13': 115169878,
    '14': 107349540,
    '15': 102531392,
    '16': 90354753,
    '17': 81195210,
    '18': 78077248,
    '19': 59128983,
    '20': 63025520,
    '21': 48129895,
    '22': 51304566,
    'X':  155270560,
    'Y':  59373566,
    'MT':  16571,

    # Haplotype contigs
    '6_apd_hap1': 4622290,
    '6_cox_hap2': 4795371,
    '6_dbb_hap3': 4610396,
    '6_mann_hap4': 4683263,
    '6_mcf_hap5': 4833398,
    '6_qbl_hap6': 4611984,
    '6_ssto_hap7': 4928567,
    '17_ctg5_hap1': 1680828,
}

# chromosome names and lengths for build 38
BUILD38_CHROMOSOMES = {
    '1':	248956422,
    '2':	242193529,
    '3':	198295559,
    '4':	190214555,
    '5':	181538259,
    '6':	170805979,
    '7':	159345973,
    '8':	145138636,
    '9':	138394717,
    '10':	133797422,
    '11':	135086622,
    '12':	133275309,
    '13':	114364328,
    '14':	107043718,
    '15':	101991189,
    '16':	90338345,
    '17':	83257441,
    '18':	80373285,
    '19':	58617616,
    '20':	64444167,
    '21':	46709983,
    '22':	50818468,
    'X':	156040895,
    'Y':	57227415,
    'MT':   16569
}


def get_data_directory():
    default = os.path.expanduser(DEFAULT_DATA_DIR)
    storage_dir = os.environ.get('DATA_DIR_VARIABLE', default)
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
