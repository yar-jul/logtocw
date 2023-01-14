import typer

from worker import worker

cli = typer.Typer()


@cli.command()
def main(
    docker_image: str = typer.Option(
        None, envvar="DOCKER_IMAGE", help="A name of a Docker image"
    ),
    bash_command: str = typer.Option(
        None,
        envvar="BASH_COMMAND",
        help="A bash command (to run inside the Docker image)",
    ),
    bash_command_file: str = typer.Option(
        None,
        envvar="BASH_COMMAND_FILE",
        help="A path to file with bash command (to run inside the Docker image)",
    ),
    container_id: str = typer.Option(
        None,
        envvar="CONTAINER_ID",
        help="Existing container ID",
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
    if not (
        docker_image and (bash_command is not None or bash_command_file) or container_id
    ):
        print("Either --docker-image or --container-id must be specified")
        exit()
    if bash_command_file is not None:
        try:
            with open(bash_command_file) as bash_command_f:
                content = bash_command_f.read()
                bash_command = content
        except Exception as exc:
            print(exc)
            exit()
    worker(
        docker_image,
        bash_command,
        aws_cloudwatch_group,
        aws_cloudwatch_stream,
        aws_access_key_id,
        aws_secret_access_key,
        awsregion,
        container_id,
    )


if __name__ == "__main__":
    cli()
