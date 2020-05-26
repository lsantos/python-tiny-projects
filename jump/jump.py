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
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args() 
    jumper = {}

    jumper['0'] = '5'
    jumper['1'] = '9'
    jumper['2'] = '8'
    jumper['3'] = '7'
    jumper['4'] = '6'
    jumper['5'] = '0'
    jumper['6'] = '4'
    jumper['7'] = '3'
    jumper['8'] = '2'
    jumper['9'] = '1'

    for c in args.text: 
        sys.stdout.write(jumper.get(c, c))
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
