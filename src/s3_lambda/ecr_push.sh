# !bin/bash

PROFILE=$1
REGION=$(aws configure --profile $PROFILE get region)
ACCOUNTID=$(aws sts get-caller-identity --profile $PROFILE --output text --query Account)
aws ecr get-login-password --profile $PROFILE | docker login --username AWS --password-stdin $ACCOUNTID.dkr.ecr.$REGION.amazonaws.com
docker push $ACCOUNTID.dkr.ecr.$REGION.amazonaws.com/rekognition_lambda:latest
DIGEST=$(aws ecr list-images --profile $PROFILE --repository-name line_bot --out text --query 'imageIds[?imageTag==`latest`].imageDigest')
echo $DIGEST
