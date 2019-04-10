import re
import os


BUILD37 = 'homo_sapiens_GRCh37'
BUILD38 = 'homo_sapiens_GRCh38'

RCRS_ACCESSION = 'NC_012920.1'

DEFAULT_DATA_DIR = '~/.seqseek'
DATA_DIR_VARIABLE = 'SEQSEEK_DATA_DIR'

URI = 'https://s3-us-west-2.amazonaws.com/seqseek/'


BUILD37_ACCESSIONS = {
    '1': 'NC_000001.10',
    '2': 'NC_000002.11',
    '3': 'NC_000003.11',
    '4': 'NC_000004.11',
    '5': 'NC_000005.9',
    '6': 'NC_000006.11',
    '7': 'NC_000007.13',
    '8': 'NC_000008.10',
    '9': 'NC_000009.11',
    '10': 'NC_000010.10',
    '11': 'NC_000011.9',
    '12': 'NC_000012.11',
    '13': 'NC_000013.10',
    '14': 'NC_000014.8',
    '15': 'NC_000015.9',
    '16': 'NC_000016.9',
    '17': 'NC_000017.10',
    '18': 'NC_000018.9',
    '19': 'NC_000019.9',
    '20': 'NC_000020.10',
    '21': 'NC_000021.8',
    '22': 'NC_000022.10',
    'X': 'NC_000023.10',
    'Y': 'NC_000024.9',
    'MT': 'NC_012920.1',
    'RSRS': 'NC_001807.4',

    # UCSC names for haplotype scaffolds
    'chr6_apd_hap1': 'NT_167244.1',
    'chr6_cox_hap2': 'NT_113891.2',
    'chr6_dbb_hap3': 'NT_167245.1',
    'chr6_mann_hap4': 'NT_167246.1',
    'chr6_mcf_hap5': 'NT_167247.1',
    'chr6_qbl_hap6': 'NT_167248.1',
    'chr6_ssto_hap7': 'NT_167249.1',
    'chr4_ctg9_hap1': 'NT_167250.1',
    'chr17_ctg5_hap1': 'NT_167251.1'
}

BUILD38_ACCESSIONS = {
    '1': 'NC_000001.11',
    '2': 'NC_000002.12',
    '3': 'NC_000003.12',
    '4': 'NC_000004.12',
    '5': 'NC_000005.10',
    '6': 'NC_000006.12',
    '7': 'NC_000007.14',
    '8': 'NC_000008.11',
    '9': 'NC_000009.12',
    '10': 'NC_000010.11',
    '11': 'NC_000011.10',
    '12': 'NC_000012.12',
    '13': 'NC_000013.11',
    '14': 'NC_000014.9',
    '15': 'NC_000015.10',
    '16': 'NC_000016.10',
    '17': 'NC_000017.11',
    '18': 'NC_000018.10',
    '19': 'NC_000019.10',
    '20': 'NC_000020.11',
    '21': 'NC_000021.9',
    '22': 'NC_000022.11',
    'X': 'NC_000023.11',
    'Y': 'NC_000024.10',
    'MT': 'NC_012920.1',
    'RSRS': 'NC_001807.4',
}

# chromosome names and lengths for build 37
ACCESSION_LENGTHS = {
    # GRCh38
    'NC_000001.11':  248956422,
    'NC_000002.12':  242193529,
    'NC_000003.12':  198295559,
    'NC_000004.12':  190214555,
    'NC_000005.10':  181538259,
    'NC_000006.12':  170805979,
    'NC_000007.14':  159345973,
    'NC_000008.11':  145138636,
    'NC_000009.12':  138394717,
    'NC_000010.11':  133797422,
    'NC_000011.10':  135086622,
    'NC_000012.12':  133275309,
    'NC_000013.11':  114364328,
    'NC_000014.9':   107043718,
    'NC_000015.10':  101991189,
    'NC_000016.10':  90338345,
    'NC_000017.11':  83257441,
    'NC_000018.10':  80373285,
    'NC_000019.10':  58617616,
    'NC_000020.11':  64444167,
    'NC_000021.9':   46709983,
    'NC_000022.11':  50818468,
    'NC_000023.11':  156040895,
    'NC_000024.10':  57227415,

    # GRCh37
    'NC_000001.10':  249250621,
    'NC_000002.11':  243199373,
    'NC_000003.11':  198022430,
    'NC_000004.11':  191154276,
    'NC_000005.9':   180915260,
    'NC_000006.11':  171115067,
    'NC_000007.13':  159138663,
    'NC_000008.10':  146364022,
    'NC_000009.11':  141213431,
    'NC_000010.10':  135534747,
    'NC_000011.9':   135006516,
    'NC_000012.11':  133851895,
    'NC_000013.10':  115169878,
    'NC_000014.8':   107349540,
    'NC_000015.9':   102531392,
    'NC_000016.9':   90354753,
    'NC_000017.10':  81195210,
    'NC_000018.9':   78077248,
    'NC_000019.9':   59128983,
    'NC_000020.10':  63025520,
    'NC_000021.8':   48129895,
    'NC_000022.10':  51304566,
    'NC_000023.10':  155270560,
    'NC_000024.9':   59373566,

    # Mito is shared between 37 & 38
    'NC_012920.1':   16569,  # rCRS
    'NC_001807.4':   16571,  # RSRS

    # Haplotype scaffolds
    'NT_113891.2': 4795371,
    'NT_167244.1': 4622290,
    'NT_167245.1': 4610396,
    'NT_167246.1': 4683263,
    'NT_167247.1': 4833398,
    'NT_167248.1': 4611984,
    'NT_167249.1': 4928567,
    'NT_167250.1': 590426,
    'NT_167251.1': 1680828,
}

MITOCHONDRIA_NAMES = {'MT', 'RSRS', BUILD37_ACCESSIONS['MT'], BUILD37_ACCESSIONS['RSRS'],
                      BUILD38_ACCESSIONS['MT'], BUILD38_ACCESSIONS['RSRS']}


def get_data_directory():
    default = os.path.expanduser(DEFAULT_DATA_DIR)
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


"""
The nine haplotype scaffolds are:
    name                    accession       UCSC chr name
    HSCHR6_MHC_APD_CTG1     GL000250.1      chr6_apd_hap1
    HSCHR6_MHC_COX_CTG1     GL000251.1      chr6_cox_hap2
    HSCHR6_MHC_DBB_CTG1     GL000252.1      chr6_dbb_hap3
    HSCHR6_MHC_MANN_CTG1    GL000253.1      chr6_mann_hap4
    HSCHR6_MHC_MCF_CTG1     GL000254.1      chr6_mcf_hap5
    HSCHR6_MHC_QBL_CTG1     GL000255.1      chr6_qbl_hap6
    HSCHR6_MHC_SSTO_CTG1    GL000256.1      chr6_ssto_hap7
    HSCHR4_1_CTG9           GL000257.1      chr4_ctg9_hap1
    HSCHR17_1_CTG5          GL000258.1      chr17_ctg5_hap1
"""
