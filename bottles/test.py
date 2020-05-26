#!/usr/bin/env python3
"""tests for bottle.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
from bottles import verse

prg = "bottles.py"

# --------------------------------------------------
def test_verse_1_bottle():
    """Test verse function with 1 bottle"""

    one = verse(1)
    assert one == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

# --------------------------------------------------
def test_verse_2_bottles():
    """Test verse function with 2 bottles"""

    two = verse(2)
    assert two == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert re.match('usage', out, re.IGNORECASE)

# --------------------------------------------------
def test_bad_num_value():
    """bad number value"""
    bad = -1
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv > 0
    assert re.search(f'-num "{bad}" must be greater than 0', out)
