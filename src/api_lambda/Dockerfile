FROM public.ecr.aws/lambda/python:3.8-arm64 AS arm64
COPY ./lambda_function/app.py   ./
CMD ["app.handler"]

FROM public.ecr.aws/lambda/python:3.8-x86_64 AS x86_64
COPY ./lambda_function/app.py   ./
CMD ["app.handler"]
