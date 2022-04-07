from venv import create
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--habit_create', default="", help='Create a habit.')
def habit(habit_create):
    """Basic functions to maintan a habit."""
    click.echo("Create habit : %s" % click.style(habit_create, fg='green'))

@click.command()
@click.option('--analyse', default="", help='Analyse a Habit.')
def analysis(analyse):
    """Basic functions to analyse a habit."""
    click.echo("Chose to analyse the habit!")

cli.add_command(habit)
cli.add_command(analysis)

if __name__ == '__main__':
    cli()

# HOW TO USE:
# python Click_POC.py habit --habit_create "Go Running"