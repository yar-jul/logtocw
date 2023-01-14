# logtocw

A Python program that send Docker container logs to CloudWatch Logs

# Installation

```bash
git clone git@github.com:yar-jul/logtocw.git
cd logtocw
poetry install
```

You can also activate the vernal environment. On Unix:

```bash
source .venv/bin/activate
```

# Usage

<div class="termy">

```console
$ logtocw --help
Usage: logtocw [OPTIONS]

Options:
  --docker-image TEXT             A name of a Docker image  [env var:
                                  DOCKER_IMAGE]
  --bash-command TEXT             A bash command (to run inside the Docker
                                  image)  [env var: BASH_COMMAND]
  --bash-command-file TEXT        A path to file with bash command (to run
                                  inside the Docker image)  [env var:
                                  BASH_COMMAND_FILE]
  --container-id TEXT             Existing container ID  [env var:
                                  CONTAINER_ID]
  --aws-cloudwatch-group TEXT     A name of an AWS CloudWatch group  [env var:
                                  AWS_CLOUDWATCH_GROUP; required]
  --aws-cloudwatch-stream TEXT    A name of an AWS CloudWatch stream  [env
                                  var: AWS_CLOUDWATCH_STREAM; required]
  --aws-access-key-id TEXT        AWS access key id  [env var:
                                  AWS_ACCESS_KEY_ID; required]
  --aws-secret-access-key TEXT    AWS secret access key  [env var:
                                  AWS_SECRET_ACCESS_KEY; required]
  --awsregion TEXT                A name of an AWS region  [env var:
                                  AWSREGION; required]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

</div>

# Example

```bash
logtocw --docker-image ubuntu --bash-command "echo hello world" --aws-cloudwatch-group g1 --aws-cloudwatch-stream s1 --aws-access-key-id ... --aws-secret-access-key ... --awsregion ...
```
