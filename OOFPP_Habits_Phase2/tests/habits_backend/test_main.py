from click.testing import CliRunner
from habits_backend.main import *

runner = CliRunner()

# def test_habit_cli():
#     """Test the habit CLI."""
#     result = runner.invoke(data, ['--add', 'Go running'])
#     assert result.exit_code == 0
#     assert 'Go running has been added.\n' in result.output


def test_seed_data():
    """Test the seeding of data."""
    result = runner.invoke(data_seed)
    assert result.exit_code == 0


def test_rest_api():
    """Test the REST API startup."""
    result = runner.invoke(start_rest_api)
    assert result.exit_code == 0


def test_analyse_streak_habit():
    """Test the analysis of a streak."""
    result = runner.invoke(analyse_streak_habit, ['--habit_id', 1])
    assert result.exit_code == 0
