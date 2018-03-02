# -*- coding: utf-8 -*-

"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later,
  but that will cause problems: the code will get executed twice:

  - When you run `python -m{{cookiecutter.package_import_name}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{cookiecutter.package_import_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{cookiecutter.package_import_name}}.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.package_cli_library|lower == 'click' %}
import click
{%- elif cookiecutter.package_cli_library|lower == 'argparse' %}
import argparse
{%- endif %}


{% if cookiecutter.package_cli_library|lower == 'click' -%}
@click.command()
@click.argument('names', nargs=-1)
def main(names):
    """Main click command."""
    click.echo(repr(names))
{% elif cookiecutter.package_cli_library|lower == 'argparse' -%}
parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    """Main function."""
    args = parser.parse_args(args=args)
    print(args.names)
{% else -%}
def main(args=None):
    """Main function."""
    print(args)
    return 0
{% endif -%}
