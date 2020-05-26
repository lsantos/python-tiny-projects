#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 26/05/2020
Purpose: Workout of the day
"""

import argparse
import os
import sys
import random
import io
import csv
from pprint import pprint
from tabulate import tabulate
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        default='inputs/exercises.csv',
                        help='CSV Input file of exercises',
                        type=argparse.FileType('r')
                        )
    
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None
                        )
    
    parser.add_argument('-n',
                        '--num',
                        default='4',
                        metavar='exercises',
                        type=int,
                        help='Number of exercises',
                        )
                    
    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()
    
    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0') 

    return args  
# --------------------------------------------------
def read_csv(fh):
    exercises = []

    if not fh:
        return exercises

    for row in csv.DictReader(fh, delimiter=','):
        name, reps = row.get('exercise'), row.get('reps')

        if name and reps:
            match = re.match('(\d+)-(\d+)', reps)

            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))
    
    return exercises

# --------------------------------------------------
def main():
    """Make some jazz noise"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)

    if not exercises:
        die(f'No usable data in --file "{args.file.name}"')

    def random_rep(triple):
        """Helper function to randomly select between the high and low reps"""
        name, low, high = triple
        rand_value = random.randint(low, high)

        return (name, int(rand_value / 2) if args.easy else rand_value)

    print(tabulate(map(random_rep, random.sample(exercises, k=args.num)), headers=('Exercise', 'Reps')))

# --------------------------------------------------
def die(msg):
    """Print msg to std.err and exit program with error code"""

    print(msg, file=sys.stderr)
    exit(1)

# --------------------------------------------------
def test_read_csv():
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

# --------------------------------------------------
if __name__ == '__main__':
    main()
