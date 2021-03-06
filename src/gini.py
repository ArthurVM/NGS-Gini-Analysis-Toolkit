#!/usr/bin/env python3

"""Calculate the Gini coefficient of coverage over a genome.
Takes a .bed format coverage file generated by the Samtools -depth utility, structured as:

'scaffold    position    depth'

in tab delimited form.

Dependancies:
Python3.6<=
argparse
numpy
"""

import argparse
import sys
import time
import os
from numpy import mean, sort, cumsum

def coverage_reader(cov_file, w):

    with open(cov_file, "r") as cov:

        lines = [int((line.split('\t')[-1]).split('\n')[0]) for line in cov.readlines()]

        if w == 1:
            return lines
        else:
            cov_array = [mean(lines[i:i+w]) for i in range(0, len(lines), w)]

    return cov_array

def gini(cov_array):
    """Calculates the Gini coefficient of a coverage array isolated from a coverage .bed file

    Maps pretty well to A/(A+B) in its functionality, but effectively calculates Gini as the mean absolute difference.
    """
    
    s_cov_array=sort(cov_array)

    cov_sum = cumsum(s_cov_array)
    height_sum = cumsum(cov_sum)
    l_area_array = height_sum - cov_sum / 2

    eq_area = cov_sum[-1] * len(cov_array) / 2  # where eq_area is the area under the line of equality

    return (eq_area - l_area_array[-1]) / eq_area

def is_file(filename):
    """Checks if a path is a file"""

    if not os.path.isfile(filename):

        msg = "{0} is not a file".format(filename)
        raise argparse.ArgumentTypeError(msg)

    else:
        return os.path.abspath(os.path.realpath(os.path.expanduser(filename)))


def is_dir(direname):
    """Checks if a path is a directory"""

    if not os.path.isdir(direname):

        msg = "{0} is not a directory".format(direname)
        raise argparse.ArgumentTypeError(msg)

    else:
        return os.path.abspath(os.path.realpath(os.path.expanduser(direname)))

def parse_args(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('script_path', action='store', help=argparse.SUPPRESS)
    parser.add_argument('cov_file', type=is_file, action='store', help='Coverage file in .bed format generated by Samtools -depth')

    parser.add_argument('-w', action='store', default=1, type=int, help='Window size. Coverage will be taken as the window mean. Default=1.')
    parser.add_argument('-G', action='store', nargs=3, default=False, type=str, help='Calculate GG curve using given range and step. Takes 3 arguments. E.g. 1 1000 5 will calculate G over window sizes 1-1000 with a step of 5. Default=False')

    args = parser.parse_args(argv)

    return args

def main(argv):

    args = parse_args(argv)

    if args.G != False:
        g_array = []
        l, u, s = args.G

        for w in range(int(l), int(u)+1, int(s)):
            cov_array = coverage_reader(args.cov_file, w)
            G=gini(cov_array)
            g_array.append(G)
            print("{window}\t{gini}".format(window=w, gini=G))

        # print g_array

    else:
        cov_array = coverage_reader(args.cov_file, args.w)
        print("{w}\t{G}".format(w=args.w, G=gini(cov_array)))

if __name__ == "__main__":
    if len(sys.argv) < 2 or "-h" in sys.argv:
        print(__doc__)
        main([sys.argv[0], "-h"])
        sys.exit(1)
    main(sys.argv)
