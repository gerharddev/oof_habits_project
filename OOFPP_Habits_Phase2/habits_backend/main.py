"""Habit Tracking Entry Point."""

import click
from habits_backend.restapi.fastapi_app import *


@click.group()
def cli():
    pass    # placeholder


@click.command()
@click.option('--command', default="", help='Command line interface for the habit tracking application.')
@click.option('--add', default="", help='Add a habit.')
def habit_cli(command, add):
    """CLI interface for habit tracking application."""
    if command:
        # TODO: Take in command line arguments for all the values
        click.echo("Command entered %s: " % command)
    if add:
        click.echo("%s has been added." % add)


@click.command()
# @click.option('--startapi',default="",help='Start the REST API with a OpenAPI documentation')
def start_rest_api():
    """Start the REST API for the habit tracking application."""
    start_api_server()


cli.add_command(habit_cli)
cli.add_command(start_rest_api)

if __name__ == '__main__':
    cli()

# HOW TO USE:
# python Click_POC.py habit --habit_create "Go Running"
# python main.py habit-cli --add test 
# python main.py rest_api --habit_api "Test"

# venv\scripts\activate - When working on the project
# deactivate - When done working on the project