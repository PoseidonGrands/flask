import sys, argparse
import click

from flask.cli import AppGroup, FlaskGroup
job_cli = AppGroup('runjob')

"""
flask runjob run -m test
flask runjob run -m test
"""
@job_cli.command('run')
@click.option('-n', '--name', metavar='name', help='指定job名')
@click.pass_context
def run(ctx, name):
    _args = sys.argv[1:]
    print(_args)

    print(name)

