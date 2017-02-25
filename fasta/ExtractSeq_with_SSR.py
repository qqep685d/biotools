"""
# Usage: python this_program.py -i input.fasta [-o output.fasta --motif "AGTA" --min_repeat 5]
"""

import sys
import argparse
import re
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input fasta file")
parser.add_argument("-o", "--output", help="Output fasta file", default=sys.stdout)
parser.add_argument("--motif", help="motif sequence", default=None)
parser.add_argument("--min_repeat", help="motif sequence", default=5)
args = parser.parse_args()

# compile index words for re.search
compiled = re.compile(r'(%s){%d,}' % (args.motif, int(args.min_repeat)))

seqs = []
for seq in SeqIO.parse(args.input, 'fasta'):
    res = compiled.search(str(seq.seq))
    if res is not None:
        seqs.append(seq)

SeqIO.write(seqs, args.output, "fasta")
