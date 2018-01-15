#!/usr/bin/env python3

"""
You can run this program from the command line:
    ./random_permutation.py

Optionally, you can give an array size:
    ./random_permutation.py 10

If you want to save the output of the program to a file I would
recommend using command-line redirection:

    ./random_permutation.py > data.txt
    ./random_permutation.py 34 > data.txt

The first line of the output stands for how many values
are generated. Each line after the first contains is a
single value, and there are not any repeated values.

"""


import random
import argparse

arg_parser = argparse.ArgumentParser(description='Generate a random permuation.')
arg_parser.add_argument('n', type=int, nargs='?', help='array size', default=10)
args = arg_parser.parse_args()

# Print the size of the output array
print(args.n)

# Create and print the permutation
permutation = list(range(args.n))
random.shuffle(permutation)
for val in permutation:
    print(val)