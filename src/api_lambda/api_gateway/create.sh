# !bin/bash

PROFILE=$1
API_NAME="func1_api"
REGION=$(aws configure --profile $PROFILE get region)

aws apigateway create-rest-api --profile $PROFILE --name $API_NAME --region $REGION
