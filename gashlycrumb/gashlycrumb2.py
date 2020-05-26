#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 04/03/2020
Purpose: Lookup tables
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashly crumb game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
                       
    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt'
                        )
                        
                                                
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dic = {line[:1].upper():line.rstrip() for line in args.file}
    
    while True:
        letter = input("Please provide a letter [! to quit]:")
        
        if letter == '!':
            print('Bye')
            break
            
        print(dic.get(letter.upper(), 'I do not know {}.'.format(letter)))
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
