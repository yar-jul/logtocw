from typer.testing import CliRunner

from src.cli import cli

runner = CliRunner()


def test_cli(without_worker, cli_args):
    result = runner.invoke(cli, cli_args)
    assert result.exit_code == 0
