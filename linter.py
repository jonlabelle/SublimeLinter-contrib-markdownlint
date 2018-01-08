#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon LaBelle
# Copyright (c) 2017 Jon LaBelle
#
# License: MIT
#

"""This module exports the Markdownlint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Markdownlint(NodeLinter):
    """Provides an interface to markdownlint."""

    syntax = ('markdown', 'markdown gfm', 'multimarkdown', 'markdown extended')
    cmd = 'markdownlint'
    npm_name = 'markdownlint-cli'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'.+?[:]\s(?P<line>\d+)[:]\s(?P<error>MD\d+)?[/]?(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
    config_file = ('--config', '.markdownlintrc', '~')
