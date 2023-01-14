import time

import boto3


class CloudwatchLogSender:
    def __init__(
        self,
        aws_access_key_id,
        aws_secret_access_key,
        region_name,
        log_group_name,
        log_stream_name,
    ):
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name
        self.token = None
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.logs = self.session.client("logs")

        try:
            response = self.logs.describe_log_streams(logGroupName=self.log_group_name)
            for log_stream in response["logStreams"]:
                if log_stream["logStreamName"] == self.log_stream_name:
                    self.token = log_stream.get("uploadSequenceToken")
            if self.token is None:
                self.logs.create_log_stream(
                    logGroupName=self.log_group_name, logStreamName=self.log_stream_name
                )
        except self.logs.exceptions.ResourceNotFoundException:
            self.logs.create_log_group(logGroupName=self.log_group_name)
            self.logs.create_log_stream(
                logGroupName=self.log_group_name, logStreamName=self.log_stream_name
            )
        except self.logs.exceptions.ResourceAlreadyExistsException:
            pass

    def put_log_event(self, timestamp, log_entry):
        if self.token:
            response = self.logs.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream_name,
                sequenceToken=self.token,
                logEvents=[{"timestamp": timestamp, "message": log_entry}],
            )
        else:
            response = self.logs.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream_name,
                logEvents=[{"timestamp": timestamp, "message": log_entry}],
            )
        self.token = response["nextSequenceToken"]

    def send_log_entry(self, log_entry):
        timestamp = round(time.time() * 1000)
        try:
            self.put_log_event(timestamp, log_entry)
        except self.logs.exceptions.ClientError:
            time.sleep(3)
            self.put_log_event(timestamp, log_entry)
