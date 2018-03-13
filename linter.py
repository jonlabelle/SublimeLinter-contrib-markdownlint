#
# linter.py
# Markdown Linter for SublimeLinter, a code checking framework
# for Sublime Text 3
#
# Written by Jon LaBelle
# Copyright (c) 2018 Jon LaBelle
#
# License: MIT
#

"""This module exports the Markdownlint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class MarkdownLint(NodeLinter):
    """Provides an interface to markdownlint."""

    syntax = ('markdown', 'markdown gfm', 'multimarkdown', 'markdown extended')
    cmd = ('markdownlint', '${args}', '${file}')
    npm_name = 'markdownlint'
    config_file = ('--config', '.markdownlintrc')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.6.0'
    check_version = True
    regex = r'.+?[:]\s(?P<line>\d+)[:]\s(?P<error>MD\d+)?[/]?(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDERR
    word_re = None
    comment_re = r'\s*/[/*]'
