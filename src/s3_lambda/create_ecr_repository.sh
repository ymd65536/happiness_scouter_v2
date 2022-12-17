# !bin/bash

PROFILE=$1
REPOSITORY_NAME="rekognition_lambda"

aws ecr create-repository --profile $PROFILE --repository-name $REPOSITORY_NAME
