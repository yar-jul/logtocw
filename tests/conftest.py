import pytest


@pytest.fixture()
def no_worker(mocker):
    mocker.patch("src.cli.worker")


@pytest.fixture
def cli_args():
    args = [
        "--docker-image",
        "python",
        "--bash-command",
        "ls",
        "--aws-cloudwatch-group",
        "test-task-group-1",
        "--aws-cloudwatch-stream",
        "test-task-stream-1",
        "--aws-access-key-id",
        "1",
        "--aws-secret-access-key",
        "1",
        "--awsregion",
        "region",
    ]
    return args
