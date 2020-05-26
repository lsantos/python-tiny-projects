#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 05/05/2020
Purpose: Rhymer
"""

import argparse
import os
import sys
import random
import string
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Make rhyming 'words'",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')    
                        

    return parser.parse_args()

# --------------------------------------------------
def stemmer(word):
    """Return lead consonants if any, and 'stem' of a word"""
    vowels = 'aeiou'
    consonants = ''.join([c for c in string.ascii_lowercase if c not in vowels])
    match = re.match(f'([{consonants}]+)?([aeiou].*)?', word.lower())

    if match:
        return (match.group(1) or '', match.group(2) or '')
    else:
        return ('', '')    


# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + ('bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr').split()
    start, rest = stemmer(args.word)

    if rest:
        print('\n'.join(sorted([prefix + rest for prefix in prefixes if prefix != start])))
    else:    
        print(f'Cannot rhyme {args.word}')
         
# --------------------------------------------------
if __name__ == '__main__':
    main()

# --------------------------------------------------
def test_stemmer():
    """ Test stemmer """
    
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
