#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 14/05/2020
Purpose: Mad libs
"""

import argparse
import os
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Mad Libs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')    
    
    parser.add_argument('-i',
                        '--inputs',
                        nargs='*',
                        metavar='input',
                        type=str,
                        help='Inputs (for testing)')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    text = args.file.read().rstrip()
    blanks = re.findall('(<([^<>]+)>)', text) 
    inputs = args.inputs
    
    if not blanks:
        print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        sys.exit(1)

    if not args.inputs:
        inputs = []
        for _, name in blanks:
            article = 'an' if name[0].lower() in 'aeiou' else 'a'
            value = input(f'Give me {article} {name}: ')
            inputs.append(value)

    while len(inputs) > 0:
        text = re.sub(r'(<([^<>]+)>)', inputs.pop(0), text, count=1)
  
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()