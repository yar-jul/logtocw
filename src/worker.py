import docker
from botocore.exceptions import BotoCoreError, ClientError
from docker.errors import DockerException

from log_sender import CloudwatchLogSender

encoding = "utf-8"
remove_container = False


def worker(
    docker_image: str,
    bash_command: str,
    aws_cloudwatch_group: str,
    aws_cloudwatch_stream: str,
    aws_access_key_id: str,
    aws_secret_access_key: str,
    awsregion: str,
    container_id: str,
):
    try:
        print("Connecting to Amazon CloudWatch")
        cloudwatch_log_sender = CloudwatchLogSender(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=awsregion,
            log_group_name=aws_cloudwatch_group,
            log_stream_name=aws_cloudwatch_stream,
        )
    except (BotoCoreError, ClientError) as exc:
        print(exc)
        exit()
    container = None
    try:
        client = docker.from_env()
        if container_id is None:
            if bash_command:
                bash_command = f"bash -c '{bash_command}'"
                print(f"Creating a new container with a command:\n\n{bash_command}\n")
            else:
                print("Creating a new container")
            container = client.containers.run(
                image=docker_image, command=bash_command, detach=True
            )
        else:
            container = client.containers.get(container_id)
        print("Streaming container's logs")
        for line in container.logs(stream=True):
            cloudwatch_log_sender.send_log_entry(line.decode(encoding))
    except DockerException as exc:
        print(exc)
        exit()
    finally:
        if container is not None and remove_container:
            container.remove(force=True)
