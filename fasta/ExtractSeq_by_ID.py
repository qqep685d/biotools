"""
# Usage: python this_program.py -i input.fasta [-o output.fasta -w "index word" -m "c"]
"""

import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input fasta file")
parser.add_argument("-o", "--output", help="Output fasta file", default=sys.stdout)
parser.add_argument("-w", "--word", help="Index word for sequence id", default=None)
parser.add_argument("-m", "--match", help="Complete match (c: default) or partial match (p)", default='c')
args = parser.parse_args()

seqs = []
for seq in SeqIO.parse(args.input, 'fasta'):
	if args.match == 'p':
		if args.word in seq.id:
			seqs.append(seq)
	else:
		if args.word == seq.id:
			seqs.append(seq)

SeqIO.write(seqs, args.output, "fasta")
