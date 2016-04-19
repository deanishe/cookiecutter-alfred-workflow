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

# Initial values for `settings.json`
DEFAULT_SETTINGS = {}

# Auto-update from GitHub releases
UPDATE_SETTINGS = {
    'github_slug': '{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
}

HELP_URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues'


def main(wf):
    """Run workflow script."""
    opts = docopt.docopt(__doc__, argv=wf.args, version=wf.version)
    query = opts.get('<query>')
    
    return 0


if __name__ == '__main__':
    wf = Workflow(
        default_settings=DEFAULT_SETTINGS,
        update_settings=UPDATE_SETTINGS,
        help_url=HELP_URL,
    )
    log = wf.logger
    sys.exit(wf.run(main))
