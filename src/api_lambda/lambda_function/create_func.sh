# !bin/bash

PROFILE=$1
FUNCTION_ROLE_NAME=$2
REPOSITORY_NAME=$3
FUNCTION_NAME=$4

REGION=$(aws configure --profile $PROFILE get region)
ACCOUNTID=$(aws sts get-caller-identity --profile $PROFILE --output text --query Account)
ROLE_ARN="arn:aws:iam::$ACCOUNTID:role/$FUNCTION_ROLE_NAME"
DIGEST=$(aws ecr list-images --profile $PROFILE --repository-name $REPOSITORY_NAME --out text --query 'imageIds[?imageTag==`latest`].imageDigest')

aws lambda create-function --profile $PROFILE --function-name $FUNCTION_NAME --package-type Image --code ImageUri=$ACCOUNTID.dkr.ecr.$REGION.amazonaws.com/func1@$DIGEST --role $ROLE_ARN
