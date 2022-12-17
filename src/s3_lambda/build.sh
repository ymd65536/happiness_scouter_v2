# !bin/bash

PROFILE=$1
STAGE_NAME=$2
FUNCTION_NAME="rekognition_lambda"

docker build --no-cache --target $STAGE_NAME -t $FUNCTION_NAME .
REGION=$(aws configure --profile $PROFILE get region)
ACCOUNTID=$(aws sts get-caller-identity --profile $PROFILE --output text --query Account)
ECR_REPOSITORY=$ACCOUNTID.dkr.ecr.$REGION.amazonaws.com/$FUNCTION_NAME:latest
echo $ECR_REPOSITORY
docker tag $FUNCTION_NAME:latest $ECR_REPOSITORY
