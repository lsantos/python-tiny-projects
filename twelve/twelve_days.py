#!/usr/bin/env python
"""
Author : Leandro Santos <leandro.bueno@globo.com>
Date   : 16/04/2020
Purpose: Twelve days of Xmas song generator
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
         
    parser.add_argument('-n',
                        '--num',
                        default=12,
                        metavar='days',
                        type=int,
                        help='Number of days to sing',
                        )

    parser.add_argument('-o',
                        '--outfile',
                        default=sys.stdout,
                        metavar='FILE',
                        help='Outfile',
                        type=argparse.FileType('wt')
                        )
                      
    args = parser.parse_args()
    
    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12') 

    return args     
    
# --------------------------------------------------
def main():
    """Make some jazz noise here"""
    args = get_args()
    args.outfile.write('\n\n'.join([verse(day) for day in range(1, args.num + 1)]))
    args.outfile.write('\n')

# --------------------------------------------------
def verse(day):
    """Create a verse"""
    ordinal = { 1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh',
                8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth' }
   
    gifts = ['A partridge in a pear tree.',
             'Two turtle doves,',
             'Three French hens,',
             'Four calling birds,',
             'Five gold rings,',
             'Six geese a laying,',
             'Seven swans a swimming,',
             'Eight maids a milking,',
             'Nine ladies dancing,',
             'Ten lords a leaping,',
             'Eleven pipers piping',
             'Twelve drummers drumming,']

    verses = [f'On the {ordinal[day]} day of Christmas,', 
             'My true love gave to me,']

    # for index in reversed(range(0, day)):
    #     if day > 1 and index == 0:
    #         verses.append(gifts[index].replace('A', 'And a'))
    #     else:         
    #         verses.append(gifts[index])

    verses.extend(reversed(gifts[:day])) 

    if day > 1:
        verses[-1] = 'And ' + verses[-1].lower()            

    return '\n'.join(verses)

# --------------------------------------------------
def test_verse():
    """Test verse"""

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
