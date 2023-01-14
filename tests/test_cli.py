from typer.testing import CliRunner

from src.cli import cli

runner = CliRunner()


def test_cli(no_worker, cli_args):
    result = runner.invoke(cli, cli_args)
    assert result.exit_code == 0


def test_cli_without_args(no_worker):
    result = runner.invoke(cli)
    assert result.exit_code == 2
