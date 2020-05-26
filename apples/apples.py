#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 09/03/2020
Purpose: Apples and bananas (find and replace)
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
        
    parser.add_argument('text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        default='a',
                        metavar='vowel',
                        choices=list('aeiou'),
                        help='The vowel to substitute',
                        )
    args = parser.parse_args()       
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
                                                
    return args

# --------------------------------------------------
def main():
    """Make some jazz noise here"""

    args = get_args()
    vowel = args.vowel
    """
    text = re.sub(r'[AEIOU]', vowel.upper(), re.sub(r'[aeiou]', vowel, args.text))
    print(text)
    """
    
    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
        
    print(''.join(map(new_char, args.text)))
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
