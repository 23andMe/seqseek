import argparse


def run(path):
    print "Formatting %s" % path
    with open(path) as fasta:
        header = ''
        first_line = fasta.readline()
        if not first_line.startswith('>'):
            header = '> ' + path.split('/')[-1].split('.')[0] + '\n'
            first_line.replace('\n', '')
        clean = fasta.read().replace('\n', '')

    with open(path + '.seqseek', 'w') as formatted:
        formatted.write(header)
        formatted.write(first_line)
        formatted.write(clean)

    with open(path + '.seqseek') as done:
        done.readline()
        sequence = done.read()
        print "Length is %d" % len(sequence)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_path")
    args = parser.parse_args()
    run(args.fasta_path)
