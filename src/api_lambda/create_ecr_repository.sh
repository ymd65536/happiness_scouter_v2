# !bin/bash

PROFILE=$1
REPOSITORY_NAME=$2

aws ecr create-repository --profile $PROFILE --repository-name $REPOSITORY_NAME
