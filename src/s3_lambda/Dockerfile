FROM public.ecr.aws/lambda/python:3.8-arm64 AS arm64
COPY ./app.py   ./
RUN pip3 install LINE-bot-sdk
CMD ["app.lambda_handler"]

FROM public.ecr.aws/lambda/python:3.8-x86_64 AS x86_64
COPY ./app.py   ./
CMD ["app.lambda_handler"]
