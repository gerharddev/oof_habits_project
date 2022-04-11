from click.testing import CliRunner

from habits_backend.main import hello

runner = CliRunner()

def test_habit_cli():
    """Test the habit CLI."""
    # runner = CliRunner()
    result = runner.invoke(hello)
    # result = runner.invoke(habit_cli, ['--add', 'new habit'])
    # assert result.exit_code == 0
    assert 'new habit has been added' in result.output