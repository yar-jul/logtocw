ENV_FILE=.env

include ${ENV_FILE}
export

.SILENT:

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## fmt: run isort and black
.PHONY: fmt
fmt:
	poetry run isort src/ tests/
	poetry run black src/ tests/

## test: run tests
.PHONY: test
test:
	poetry run python -m pytest

## case1: case 1
.PHONY: case1
case1:
	logtocw --docker-image bfirsh/reticulate-splines --bash-command "" --aws-cloudwatch-stream case1

## case2: case 2
.PHONY: case2
case2:
	logtocw --docker-image python --bash-command 'pip install pip -U && pip install tqdm' --aws-cloudwatch-stream case2

## case3: case 3
.PHONY: case3
case3:
	logtocw --docker-image python --bash-command-file commands/command_1 --aws-cloudwatch-stream case3
