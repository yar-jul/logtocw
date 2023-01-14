import typer

from worker import worker

cli = typer.Typer()


@cli.command()
def main(
    docker_image: str = typer.Option(
        ..., envvar="DOCKER_IMAGE", help="A name of a Docker image"
    ),
    bash_command: str = typer.Option(
        "",
        envvar="BASH_COMMAND",
        help="A bash command (to run inside the Docker image)",
    ),
    aws_cloudwatch_group: str = typer.Option(
        ..., envvar="AWS_CLOUDWATCH_GROUP", help="A name of an AWS CloudWatch group"
    ),
    aws_cloudwatch_stream: str = typer.Option(
        ..., envvar="AWS_CLOUDWATCH_STREAM", help="A name of an AWS CloudWatch stream"
    ),
    aws_access_key_id: str = typer.Option(
        ..., envvar="AWS_ACCESS_KEY_ID", help="AWS access key id"
    ),
    aws_secret_access_key: str = typer.Option(
        ..., envvar="AWS_SECRET_ACCESS_KEY", help="AWS secret access key"
    ),
    awsregion: str = typer.Option(
        ..., envvar="AWSREGION", help="A name of an AWS region"
    ),
):
    worker(
        docker_image,
        bash_command,
        aws_cloudwatch_group,
        aws_cloudwatch_stream,
        aws_access_key_id,
        aws_secret_access_key,
        awsregion,
    )


if __name__ == "__main__":
    cli()
