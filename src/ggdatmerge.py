#!/usr/bin/env python3

"""Generate a .tsv format file from an arbitrary number of files generated by gini.py, structured as:

W    D1   D2   D3  ...
1     G    G    G  ...
2     G    G    G  ...
3     G    G    G  ...
...

Where Dn refers to a dataset, W refers to window size, and G is the Gini.

Dependancies:
Python3.6<=
argparse
pandas
"""

import argparse
import sys
import re
import pandas as pd
from os import path

def merge_GG_files(args):
    ## reads in a GG files and merges
    in_files = args.Gini_files

    pd_array = [pd.read_csv(p, sep="\t", parse_dates=True, index_col=0, names=["W", path.splitext(path.basename(p))[0]]) \
    for p in in_files]

    pd.concat(pd_array, axis=1, join="outer").to_csv(args.o, sep="\t")

def parse_args(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('script_path', action='store', help=argparse.SUPPRESS)

    parser.add_argument('--Gini_files', nargs='*', action='store', help='Files generated by gini.py to merge. E.g. file_1 file_2 file_3 ...')
    parser.add_argument('-o', action='store', default="gini-merge.GG", type=str, help='Meged file output name. Default = gini-merge.GG')

    args = parser.parse_args(argv)

    return args

def main(argv):

    args = parse_args(argv)

    merge_GG_files(args)

if __name__ == "__main__":
    if len(sys.argv) <= 2 or "-h" in sys.argv:
        print(__doc__)
        main([sys.argv[0], "-h"])
        sys.exit(1)
    main(sys.argv)
