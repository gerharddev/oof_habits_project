"""Habit Tracking Entry Point."""

# TODO:
# Setup pylint
# Setup pytest
# Seed the database with some habits
# CLI interface
# Swagger Interface
# venv\scripts\activate
# deactivate

# from venv import create #Virtual Environment - virtualenv
import click

@click.group()
def cli():
    pass

def hello():
    click.echo('Hello World!')

my_test = "HELLO"

@click.command()
@click.option('--add', default="", help='Add a new habit.')
def habit_cli(add):
    """CLI interface for habit tracking application."""
    click.echo("New Habit: %s" % add)

@click.command()
@click.option('--habit_api', default="", help='REST Api for the habit tracking application.')
def rest_api(habit_api):
    """REST API for habit tracking application."""
    click.echo("API!")

cli.add_command(habit_cli)
cli.add_command(rest_api)

if __name__ == '__main__':
    print('STARTING')
    cli()

# HOW TO USE:
# python Click_POC.py habit --habit_create "Go Running"
# python main.py habit-cli --add test 