#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 16/04/2020
Purpose: Ransom Note
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
        
    parser.add_argument('text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        default=None,
                        metavar='int',
                        help='Random seed',
                        )
    args = parser.parse_args()       
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
                                                
    return args

# --------------------------------------------------
def main():
    """Make some jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    #print(''.join(map(choose, args.text)))
    print(''.join([choose(char) for char in args.text])) 
# --------------------------------------------------
def choose(letter):
    """randomly choose an upper or lower letter to return"""

    return letter.upper() if random.choice([False, True]) else letter.lower()

# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)

    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'

    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()


