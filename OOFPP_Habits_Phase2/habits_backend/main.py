"""Habit Tracking Entry Point."""

# venv\scripts\activate - When working on the project 

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
    pass    # placeholder

def hello():
    click.echo('Hello World!')

my_test = "HELLO"

@click.command()
@click.option('--command', default="", help='Command line interface for the habit tracking application.')
@click.option('--add', default="", help='Add a habit.')
def habit_cli(command,add):
    """CLI interface for habit tracking application."""
    if command:
        # TODO: Take in command line arguments for all the values
        click.echo("Command entered %s: "%(command))
    if add:
        click.echo("Adding a new  %s habit."%(add))

@click.command()
def start_rest_api():
    """Start the REST API for the habit tracking application."""

    click.echo("START REST API")

cli.add_command(habit_cli)
cli.add_command(start_rest_api)

if __name__ == '__main__':
    cli()

# HOW TO USE:
# python Click_POC.py habit --habit_create "Go Running"
# python main.py habit-cli --add test 
# python main.py rest_api --habit_api "Test"
