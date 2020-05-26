#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 12/02/2020
Purpose: Scramble the letters of words
"""

import argparse
import os
import sys
import random
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')    
                                                
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None
                        )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args     

# --------------------------------------------------
def scramble(word):
    """For words over 3 characters, shuffle the letters in the middle"""
    
    if len(word) < 4 or re.match(r'^\W+', word):
        return word

    begin = word[:1]     
    middle = list(word[1:-1])
    random.shuffle(middle)
    end = word[-1:]

    return begin + ''.join(middle) + end

# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        #print(''.join([scramble(word) for word in splitter.split(line)]))
        print(''.join(map(scramble, splitter.split(line))))
 
         
# --------------------------------------------------
if __name__ == '__main__':
    main()

def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"

    random.setstate(state)