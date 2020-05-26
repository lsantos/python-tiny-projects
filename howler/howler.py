#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 28/02/2020
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='A positional argument')
                        
    parser.add_argument('-o',
                        '--outfile',
                        help='A file path to write to',
                        metavar='str',
                        type=str,
                        default='')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input
    output = args.outfile
    howler = ""
    
    try:
        with open(input) as file:
            howler = file.read().rstrip().upper()
        
        if output:
            with open(output, 'w') as file:
                file.write(howler)
        else:
            print(howler)
        
    except IOError:
        howler = input.upper()
        print(howler)

# --------------------------------------------------
if __name__ == '__main__':
    main()
