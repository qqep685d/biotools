"""
# Usage: python this_program.py -i input.fasta [-o output.fasta -w "index sequence"]
"""

import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input fasta file")
parser.add_argument("-o", "--output", help="Output fasta file", default=sys.stdout)
parser.add_argument("-w", "--word", help="Index sequence", default=None)
args = parser.parse_args()

seqs = []
for seq in SeqIO.parse(args.input, 'fasta'):
	if args.word in seq.seq:
		seqs.append(seq)

SeqIO.write(seqs, args.output, "fasta")
