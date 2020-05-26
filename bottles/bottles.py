#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 15/04/2020
Purpose: Bottle song generator
"""

import argparse
import os
import sys
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
         
    parser.add_argument('-n',
                        '--num',
                        default=10,
                        metavar='num',
                        type=int,
                        help='How many bottles',
                        )
                        
    args = parser.parse_args()
    
    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0') 

    return args     
    
# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()

    print('\n\n'.join(map(verse, range(args.num, 0, -1))))
 
 # --------------------------------------------------
def verse(num):
    """Sing a verse"""
    verses = []
    suffix = '' if num == 1 else 's'

    verses.append(f'{num} bottle{suffix} of beer on the wall,')
    verses.append(f'{num} bottle{suffix} of beer,')
    verses.append('Take one down, pass it around,')

    if num == 1:
        verses.append('No more bottles of beer on the wall!')
    else:        
        verses.append(f'{num -1} bottle of beer on the wall!')

    return '\n'.join(verses)

# --------------------------------------------------
if __name__ == '__main__':
    main()
