#!/usr/bin/env python
# coding=utf8

# see README file for details

import argparse
import os
import sys

DEFAULT_COMMANDS = ['google-chrome', 'chromium-browser']


# this has been stolen from
# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


parser = argparse.ArgumentParser()
parser.add_argument('mailto', nargs='?', help=(
    'Can either be a mailto link, in which case a new mail window will be '
    'opened or nothing, to open the inbox.'), default=None)
parser.add_argument('--cmd', default=None, help=(
    'Which command to use for opening chrome/chromium. If not set, '
    '%r are tried in order.' % (DEFAULT_COMMANDS)
))
parser.add_argument('-v', '--verbose', default=False, action='store_true',
                    help='Show command before running it.')
parser.add_argument('-n', '--dry-run', default=False, action='store_true',
                    help='Don\'t actually run anything.')
args = parser.parse_args()

cmd = [args.cmd or reduce(lambda c, n: c or which(n), DEFAULT_COMMANDS, None)]

if not args.mailto:
    cmd.append('--app=https://mail.google.com/mail')
else:
    cmd.append('--app=https://mail.google.com/mail?extsrc=mailto&url=%s'
                    % args.mailto)

if args.verbose:
    print ' '.join(cmd)

if not args.dry_run:
    os.execv(cmd[0], cmd)
