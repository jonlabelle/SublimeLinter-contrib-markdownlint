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

    defaults = {
        'selector': 'text.html.markdown,'
                    'text.html.markdown.multimarkdown,'
                    'text.html.markdown.extended,'
                    'text.html.markdown.gfm'
    }
    cmd = ('markdownlint', '${args}', '${file}')
    regex = r'.+?(?:[:](?P<line>\d+))(?:[:](?P<col>\d+))?\s+(?P<error>MD\d+)?[/]?(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDERR
    word_re = None
