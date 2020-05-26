#!/usr/bin/env python3
"""tests for ransom.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re

prg = "ransom.py"
file_input = "../inputs/fox.txt"
bad_file_input = "../tmp/no_exist.txt"
# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert re.match('usage', out, re.IGNORECASE)

# --------------------------------------------------
def test_input_file():
    """test with file input"""
    out = getoutput(f'{prg} -s 3 {file_input}')
    assert re.match('THe QuIck BRoWn foX jUmps OvER the LAzY DOg.', out)

# --------------------------------------------------
def test_bad_input_file():
    """test with bad file input"""
    out = getoutput(f'{prg} -s 3 {bad_file_input}')
    assert re.match('', out)
