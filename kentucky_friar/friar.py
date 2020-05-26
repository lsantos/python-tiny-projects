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

def fry(word):
    """fry a word testing for vowel before ing"""
    fried_word = word
    you_match = re.match('^([Y|y])ou$', word)
    ing_word = re.search('(.+)ing$', word)

    if you_match:
        fried_word = f"{you_match.group(1)}'all"
    elif ing_word:
        first = ing_word.group(1)

        if re.search('[aeiouy]', first, re.IGNORECASE):
            fried_word = first + "in'"         

    return fried_word

def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"

# --------------------------------------------------
def main():
    """Make some jazz noise here"""

    args = get_args()
   
    for line in args.text.splitlines():
        #print(''.join(map(fry, [word for word in re.split(r'(\W+)', line)])))
        print(''.join([fry(word) for word in re.split(r'(\W+)', line)]))

# --------------------------------------------------
if __name__ == '__main__':
    main()
