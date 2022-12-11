# !bin/bash

PROFILE=$1
STAGE_NAME=$2
FUNC_NAME=$3

docker build --no-cache --target $STAGE_NAME -t $FUNC_NAME .
REGION=$(aws configure --profile $PROFILE get region)
ACCOUNTID=$(aws sts get-caller-identity --profile $PROFILE --output text --query Account)
ECR_REPOSITORY=$ACCOUNTID.dkr.ecr.$REGION.amazonaws.com/$FUNC_NAME:latest
echo $ECR_REPOSITORY
docker tag $FUNC_NAME:latest $ECR_REPOSITORY
