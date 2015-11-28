# encoding: utf-8
#
# Copyright (c) 2015 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-11-28
#

"""
Called after project is generated.

Install Alfred-Workflow and docopt.
"""

from __future__ import unicode_literals, print_function

import subprocess
import sys

packages = [
    'Alfred-Workflow',
    'docopt',
]

cmd = ['/usr/bin/python', '-m', 'pip', 'install', '--target', 'src'] + packages

print("Installing packages : {} ...".format(', '.join(packages)),
      file=sys.stderr)

subprocess.call(cmd)
