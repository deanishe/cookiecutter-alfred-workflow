#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on {{ cookiecutter.date }}
#

"""{{ cookiecutter.script_name }} [options] [args]

Usage:
    {{ cookiecutter.script_name }} <query>
    {{ cookiecutter.script_name }} -h | --help
    {{ cookiecutter.script_name }} --version

Options:
    -h, --help      Show this message and exit.
    --version       Show version number and exit.

"""

from __future__ import print_function, unicode_literals, absolute_import

import sys

import docopt
from workflow import Workflow

log = None


def main(wf):
    """Run workflow script."""
    opts = docopt.docopt(__doc__, argv=wf.args, version=wf.version)
    query = opts.get('<query>')


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
