#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 08/05/2020
Purpose: Kentucky Friar
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
        
    parser.add_argument('text',
                        help='Input text or file')

    args = parser.parse_args()       
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
                                                
    return args

# --------------------------------------------------
def main():
    """Make some jazz noise here"""

    args = get_args()
    vowels = 'aeiou'
    """
    text = re.sub(r'[AEIOU]', vowel.upper(), re.sub(r'[aeiou]', vowel, args.text))
    print(text)
    """

    print(args)

    for line in args.text.splitlines():
        print(line)

# --------------------------------------------------
if __name__ == '__main__':
    main()
