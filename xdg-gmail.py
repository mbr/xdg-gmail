#!/usr/bin/env python
# coding=utf8

# see README file for details

import os
import sys

if 1 == len(sys.argv):
	inbox_command = 'chromium-browser'
	inbox_args = [inbox_command, '--app=https://mail.google.com/mail']

	os.execvp(inbox_command, inbox_args)
else:
	mailto_command = 'chromium-browser'
	mailto_args = [mailto_command, '--app=https://mail.google.com/mail?extsrc=mailto&url=%s' % sys.argv[1]]

	os.execvp(mailto_command, mailto_args)
