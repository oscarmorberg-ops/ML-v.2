FROM public.ecr.aws/lambda/python:3.12

# Installera deps
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT}

# Kopiera HELA src/
COPY src/ ${LAMBDA_TASK_ROOT}/

CMD ["realtime.lambda_handler.handler"]
