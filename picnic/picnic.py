#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : today
Purpose: Picnic Game
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Show list of food items for the picnic"""

    args = get_args()
    items = args.item
    sep = ", "
    conj = " and "
    bringing = ""
    num = len(items)
    
    if (args.sorted):
        items.sort()
     
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = conj.join(items)
    else:
        bringing = sep.join(items[:-1]) + conj + items[-1]

    print "You are bringing {}".format(bringing)

# --------------------------------------------------
if __name__ == '__main__':
    main()
