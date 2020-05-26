#!/usr/bin/env python3
"""tests for rhymer.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "rhymer.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------

def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert re.match('usage', out, re.IGNORECASE)
