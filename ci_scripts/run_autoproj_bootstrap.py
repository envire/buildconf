#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' <path/to/autoproj_bootstrap> <path/to/buildconf>')
    sys.exit(1)

# Note that, for Python 3 compatibility reasons, we are using spawnu and
# importing unicode_literals (above). spawnu accepts Unicode input and
# unicode_literals makes all string literals in this script Unicode by default.
child = pexpect.spawnu('ruby2.0 ' + sys.argv[1] + ' git ' + sys.argv[2])
child.logfile = sys.stdout

try:
    child.expect_exact('So, what do you want ? (all, none or a comma-separated list of: os gem pip) [all] ')
    child.sendline('')

    child.expect(pexpect.EOF, timeout=300)
except pexpect.EOF:
    print('\n\nPEXPECT: CHILD EXITED BEFORE ALL EXPECTED INPUTS WERE READ!\n')
    sys.exit(1)
except pexpect.TIMEOUT:
    print('\n\nPEXPECT: TIMEOUT!\n')
    sys.exit(1)

child.close()
sys.exit(child.exitstatus)
