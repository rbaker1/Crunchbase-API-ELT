FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Copy lambda function code and install requirements
COPY . .

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
ADD . .

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG CB_API_KEY_PROD
ARG BUCKET_DESTINATION

ENV AWS_ACCESS_KEY_ID ${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY ${AWS_SECRET_ACCESS_KEY}
ENV CB_API_KEY_PROD ${CB_API_KEY_PROD}
ENV BUCKET_DESTINATION ${BUCKET_DESTINATION}


# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]