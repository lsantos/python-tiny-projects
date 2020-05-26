#!/usr/bin/env python3
"""tests for bottle.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re

prg = "twelve_days.py"

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
    assert re.search(f'-num "{bad}" must be between 1 and 12', out)
