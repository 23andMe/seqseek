import argparse
from .chromosome import BUILD37_ACCESSIONS, Chromosome
from .lib import BUILD37, BUILD38


PROGRAM_TO_ASSEMBLY = {
    'seqseek_37': BUILD37,
    'seqseek_38': BUILD38
}
RELATIVE_SIGNS = ('-', '+')
SIGN_FACTOR = {
    '-': -1,
    '+': 1
}


def determine_start_end(arg_start, arg_end):
    relative_start, relative_end = None, None
    if arg_start[0] in RELATIVE_SIGNS:
        relative_start, arg_start = arg_start[0], arg_start[1:]
    if arg_end[0] in RELATIVE_SIGNS:
        relative_end, arg_end = arg_end[0], arg_end[1:]

    if relative_start is not None and relative_end is not None:
        raise ValueError('Start and end cannot be both relative.')

    start, end = int(arg_start), int(arg_end)

    if relative_start is not None:
        start = end + SIGN_FACTOR[relative_start] * start
    elif relative_end is not None:
        end = start + SIGN_FACTOR[relative_end] * end

    return start, end


def cmd_line():
    parser = argparse.ArgumentParser(description='Print sequence')
    parser.add_argument('chromosome', type=str, help='Chromosome name to seek')
    parser.add_argument('start', type=str, help='Start position (can be relative, e.g. -50)')
    parser.add_argument('end', type=str, help='End position (can be relative, e.g. +50)')
    args = parser.parse_args()
    assembly = PROGRAM_TO_ASSEMBLY[parser.prog]

    # Do it
    kwargs = {'loop': True} if args.chromosome in ('MT', BUILD37_ACCESSIONS['MT']) else {}
    c = Chromosome(args.chromosome, assembly=assembly, **kwargs)
    start, end = determine_start_end(args.start, args.end)
    print(c.sequence(start, end))
