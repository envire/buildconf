#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import sys

# Note that, for Python 3 compatibility reasons, we are using spawnu and
# importing unicode_literals (above). spawnu accepts Unicode input and
# unicode_literals makes all string literals in this script Unicode by default.
child = pexpect.spawnu('amake')
child.logfile = sys.stdout

try:
    child.expect_exact('used for pulling and the second one for pushing [http,ssh] ')
    child.sendline('')
    child.expect_exact('used for pulling and the second one for pushing [http,ssh] ')
    child.sendline('')
    child.expect_exact('See http://rock-robotics.org/stable/documentation/installation.html for more information [stable] ')
    child.sendline('master')
    child.expect_exact("Please answer 'yes' or 'no' [no] ")
    child.sendline('')
    child.expect_exact('the target operating system for Orocos/RTT (gnulinux, xenomai, or macosx) [gnulinux] ')
    child.sendline('')
    child.expect_exact("Answer 'none' to disable CORBA, otherwise pick either tao or omniorb [omniorb] ")
    child.sendline('')
    # only on Debian Jessie, not on Ubuntu Trusty:
    #child.expect_exact('whether C++11 should be enabled for Rock packages [no] ')
    #child.sendline('')

    child.expect_exact('autoproj: importing and loading selected packages')
    child.expect(pexpect.EOF, timeout=7200)
except pexpect.EOF:
    print('\n\nPEXPECT: CHILD EXITED BEFORE ALL EXPECTED INPUTS WERE READ!\n')
    sys.exit(1)
except pexpect.TIMEOUT:
    print('\n\nPEXPECT: TIMEOUT!\n')
    sys.exit(1)

child.close()
sys.exit(child.exitstatus)
