#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 25/05/2020
Purpose: Gematria
"""

import argparse
import os
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria",
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
  
    for line in args.text.splitlines():
        print(' '.join([word2num(word) for word in line.split()]))

# --------------------------------------------------
def word2num(word):
    """Return string that represents the sum of the input word's ascii characters"""
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))

# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"

# --------------------------------------------------
if __name__ == '__main__':
    main()