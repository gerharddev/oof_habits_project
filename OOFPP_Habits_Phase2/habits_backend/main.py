"""Habit Tracking Entry Point."""

import click
from habits_backend.restapi.fastapi_app import *
from habits_backend.services.seed import seeding_service
from habits_backend.services.analysis import analysis_service


@click.group()
def cli():
    pass    # placeholder


@click.command()
def data_seed():
    """Load testing data into the database."""
    click.echo("Seed")


@click.command()
def data_clear():
    """Clear habit data from the database."""
    click.echo("Clear")



@click.command()
def analyse_tracked_habits():
    """Return a list of tracked habits. """
    tracked = analysis_service.get_tracked_habits()
    click.echo("Tracked Habits: ")
    click.echo(tracked)


@click.command()
@click.option('--frequency', default="daily", help='Frequency e.g. daily,weekly,monthly')
def analyse_equal_periodicity(frequency):
    """Return a list of habits with equal periodicity. """
    tracked = analysis_service.get_equal_periodicity(frequency)
    click.echo("Equal Periodicity: ")
    click.echo(tracked)


@click.command()
@click.option('--habit_id', default="", help='Habit id e.g. 1')
def analyse_streak_habit(habit_id):
    """Return the start and end date for a streak with the number of time a habit was completed. """
    streak = analysis_service.get_streak_by_habit_id(habit_id)
    click.echo("Streak Details: ")
    click.echo(streak)


@click.command()
def analyse_longest_streak():
    """Return the longest streak for any habit (Most consecutive times a habit was completed). """
    streak = analysis_service.get_longest_streak()
    click.echo("Longest Streak any habit: ")
    click.echo(streak)


@click.command()
def start_rest_api():
    """Start the REST API for the habit tracking application."""
    start_api_server()


# TODO: Seeding of data
cli.add_command(data_seed)
cli.add_command(data_clear)
cli.add_command(analyse_tracked_habits)
cli.add_command(analyse_equal_periodicity)
cli.add_command(analyse_streak_habit)
cli.add_command(analyse_longest_streak)
cli.add_command(start_rest_api)

if __name__ == '__main__':
    seeding_service.frequencies()
    # TODO: Move seed and clear to operations
    seeding_service.sample_data()
    cli()

# HOW TO USE:
# python Click_POC.py habit --habit_create "Go Running"
# python main.py habit-cli --add test 
# python main.py rest_api --habit_api "Test"

# venv\scripts\activate - When working on the project
# deactivate - When done working on the project