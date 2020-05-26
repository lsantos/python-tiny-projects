#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 02/03/2020
Purpose: Emulate wc (word count)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        help='Input files',
                        type=argparse.FileType('r')
                        )
                                                
    return parser.parse_args()

# --------------------------------------------------
def main():
    """"""

    args = get_args()
    files = args.files
    total_lines, total_words, total_chars = 0, 0, 0
         
    for fh in files:
        num_chars, num_lines, num_words = 0, 0, 0
        for line in fh:
            num_lines  += 1
            num_words += len(line.split())
            num_chars += len(line)
            
        total_lines += num_lines        
        total_chars += num_chars
        total_words += num_words
            
        print("{:8d} {:8d} {:8d} {:8}".format(num_lines, num_words, num_chars, fh.name))
    
    if len(files) > 1:
       print("{:8d} {:8d} {:8d} total".format(total_lines, total_words, total_chars))

# --------------------------------------------------
if __name__ == '__main__':
    main()
