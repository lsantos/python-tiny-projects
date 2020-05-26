#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 10/03/2020
Purpose: Dial a curse
"""

import argparse
import os
import sys
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Dial a curse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
    parser.add_argument('-a',
                        '--adjectives',
                        default='2',
                        metavar='adjectives',
                        type=int,
                        help='Number of adjectives',
                        )
                        
    parser.add_argument('-n',
                        '--insults',
                        default='3',
                        metavar='insults',
                        type=int,
                        help='Number of insults',
                        )
                        
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None
                        )
    args = parser.parse_args()
    
    if args.adjectives < 1:
        parser.error("--adjectives {} must be > 0".format(args.adjectives)) 
        
    if args.insults < 1:
        parser.error("--insults {} must be > 0".format(args.insults))        
        
    return args     
    
# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    nouns = """
                        Judas Satan ape ass barbermonger beggar block boy braggart 
                        butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger 
                        fool gull harpy jack jolthead knave liar lunatic maw peevishunmannered minion 
                        ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.split()
    
    adjectives = """
                        bankrupt base caterwauling corrupt cullionly detestable dishonest false 
                        filthsome filthy foolish foul gross heedless indistinguishable infected 
                        insatiate irksome lascivious lecherous loathsome lubbery old peevish 
                        rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced 
                        toad-spotted unmannered vile wall-eyed
    """.split()
      
    random.seed(args.seed)

    for _ in range(args.insults):
        print("You {} {}!".format(", ".join(random.sample(adjectives, args.adjectives)), random.choice(nouns)))
        
         
# --------------------------------------------------
if __name__ == '__main__':
    main()
