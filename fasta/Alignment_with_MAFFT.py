"""
[usage example] pyhton [this_program].py -i input_fasta [-o output_fasta --mafft_exe path_to_mafft_program]
"""

from Bio.Align.Applications import MafftCommandline
from Bio import AlignIO
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input fasta file")
parser.add_argument("-o", help="Output fasta file", default=None)
parser.add_argument("--mafft_exe", help="If the mafft binary is not on the path, you need to supply the executable location", default=None)
args = parser.parse_args()

if args.mafft_exe is None:
    mafft_cline = MafftCommandline(input=args.i)
else:
    mafft_cline = MafftCommandline(args.mafft_exe, input=args.i)

stdout, stderr = mafft_cline()
if args.o is None:
    print(stdout)
else:
    with open(args.o, "w") as handle:
        handle.write(stdout)
