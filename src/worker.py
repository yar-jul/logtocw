import docker

from log_sender import CloudwatchLogSender


def worker(
    docker_image: str,
    bash_command: str,
    aws_cloudwatch_group: str,
    aws_cloudwatch_stream: str,
    aws_access_key_id: str,
    aws_secret_access_key: str,
    awsregion: str,
):
    cloudwatch_log_sender = CloudwatchLogSender(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=awsregion,
        log_group_name=aws_cloudwatch_group,
        log_stream_name=aws_cloudwatch_stream,
    )
    client = docker.from_env()
    container = client.containers.run(
        image=docker_image, command=bash_command, detach=True
    )
    for line in container.logs(stream=True):
        cloudwatch_log_sender.send_log_entry(str(line).strip())
