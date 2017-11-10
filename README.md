# Sublime Text Markdownlint

[![Travis Build Status](https://travis-ci.org/jonlabelle/SublimeLinter-contrib-markdownlint.svg?branch=master)](https://travis-ci.org/jonlabelle/SublimeLinter-contrib-markdownlint "Travis Build Status")

> A Sublime Text plug-in for linting Markdown/CommonMark files.

![Markdownlint Screenshot](screenshots/screenshot.png "Markdownlint Screenshot")

## Installing

[SublimeLinter 3] must be installed in order to use this plug-in. If
SublimeLinter 3 is not installed, please follow the instructions outlined
[here][installation].

### Install Markdownlint

Before using this plug-in, you must ensure that [markdownlint][CLI] is
installed on your system. To install `markdownlint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).
2. Install `markdownlint` by typing the following in a terminal:
```bash
npm install -g markdownlint-cli
```
3. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in
   `.zshenv` and not `.zshrc`.
4. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plug-in for
   `oh-my-zsh`.

### Markdownlint Configuration

In order for `markdownlint` to be executed by SublimeLinter, you must ensure
that its path is available to SublimeLinter. Before going any further, please
read and follow the steps in ["Finding a linter executable"](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable)
through "Validating your PATH" in the documentation.

Once you have installed and configured `markdownlint`, you can proceed to
install the SublimeLinter-contrib-markdownlint plug-in if it is not yet
installed.

### Install Sublime Text Markdownlint

Please use [Package Control][pc] to install Sublime Text Markdownlint. This will
ensure that the plug-in will be updated when new versions are available. If you
want to install from source so you can modify the source code, you probably know
what you are doing so we won't cover that here.

To install via [Package Control][pc], do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`.
   Among the commands you should see `Package Control: Install Package`. If that
   command is not highlighted, use the keyboard or mouse to select it. There
   will be a pause of a few seconds while Package Control fetches the list of
   available plug-ins.
2. When the plug-in list appears, type `markdownlint`. Among the entries you
   should see `SublimeLinter-contrib-markdownlint`. If that entry is not
   highlighted, use the keyboard or mouse to select it.

### Sublime Text Markdownlint Configuration

Configuring the plug-in is done through [linter settings][linter-settings].

To ensure `markdownlint` configuration is accessible to the plug-in, use [`chdir` setting] to ensure `markdownlint` is executed relative to your configuration file.

## Contributing

If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plug-in repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don't be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very
  well known.

## Author

Jon LaBelle

## License

[MIT License]

[SublimeLinter 3]: http://www.sublimelinter.com
[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://packagecontrol.io/packages/SublimeLinter-contrib-markdownlint
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[`chdir` setting]: http://sublimelinter.readthedocs.io/en/latest/linter_settings.html#chdir
[markdownlint]: https://github.com/DavidAnson/markdownlint
[`markdownlint`]: https://github.com/DavidAnson/markdownlint
[CLI]: https://github.com/igorshubovych/markdownlint-cli
[MIT License]: LICENSE.txt
