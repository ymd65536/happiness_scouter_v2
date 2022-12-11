# !bin/bash

PROFILE=$1
FUNCTION_NAME=$2

aws lambda invoke --profile $PROFILE --function-name $FUNCTION_NAME output
cat output
