from click.testing import CliRunner
from habits_backend.main import *

runner = CliRunner()

def test_habit_cli():
    """Test the habit CLI."""
    result = runner.invoke(habit_cli, ['--add', 'Go running'])
    assert result.exit_code == 0
    assert 'Go running has been added.\n' in result.output

def test_rest_api():
    """Test the REST API startup"""
    result = runner.invoke(start_rest_api,['--startapi'])
    assert result.exit_code == 0
