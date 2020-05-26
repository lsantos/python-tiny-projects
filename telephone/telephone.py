#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 30/03/2020
Purpose: Telephone game
"""

import argparse
import os
import sys
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')    
                        
    parser.add_argument('-m',
                        '--mutations',
                        default=0.1,
                        metavar='mutations',
                        type=float,
                        help='Percent mutations',
                        )
                        
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
    
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1') 

    return args     
    
# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    alpha = string.ascii_letters + string.punctuation
    len_text = len(args.text)
    num_mutations = round(args.mutations * len_text)
    new_text = args.text
    print(f'You said: "{args.text}"')
    new_char = ''

    for i in random.sample(range(len_text), num_mutations):
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i+1:]

    print(f'I heard : "{new_text}"')
 
         
# --------------------------------------------------
if __name__ == '__main__':
    main()
