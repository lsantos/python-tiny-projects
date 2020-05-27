#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 27/05/2020
Purpose: Password maker
"""

import argparse
import os
import sys
import re
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Password maker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        default='C://Users//leand//dict',
                        type=argparse.FileType('r')
                        )

    parser.add_argument('-n',
                        '--num',
                        default='3',
                        metavar='num_passwords',
                        type=int,
                        help='Number of passwords to generate',
                        )

    parser.add_argument('-w',
                        '--num_words',
                        default='4',
                        metavar='words',
                        type=int,
                        help='Number of words to use for password',
                        )

    parser.add_argument('-m',
                        '--min_word_len',
                        default='3',
                        metavar='min_word_len',
                        type=int,
                        help='Minimum word length',
                        )

    parser.add_argument('-x',
                        '--max_word_len',
                        default='6',
                        metavar='max_word_len',
                        type=int,
                        help='Maximum word length',
                        )

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None
                        )

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')
   
    args = parser.parse_args()       
                                                
    return args

# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len  

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.title().split())):
                words.add(word)
    
    words = sorted(words)
    passwords = [''.join(random.sample(words, args.num_words)) for _ in range(args.num)]
    
    if args.l33t:
        passwords = [l33t(password) for password in passwords]

    print('\n'.join(passwords))    
 
# --------------------------------------------------
def clean(word):
    if not word:
        return ''

    return re.sub(r'\W+', '', word)      

# --------------------------------------------------
def ransom(word):
    if not word:
        return ''

    return ''.join([letter.upper() if random.choice([False, True]) else letter.lower() for letter in word])

# --------------------------------------------------
def l33t(word):
    if not word:
        return ''

    table = {'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3','I': '1', 'S': '5'}

    return ransom(word).translate(str.maketrans(table)) + random.choice(string.punctuation)

# --------------------------------------------------
if __name__ == '__main__':
    main()