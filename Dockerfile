FROM python:3.8

# Copy function code
COPY /crunchbase_extract /crunchbase_extract
COPY /boto3s3 /boto3s3
COPY app.py .


# Install the function's dependencies using file requirements.txt
# from your project folder
RUN pip install --upgrade pip
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt

ARG CB_API_KEY_PROD
ARG BUCKET_DESTINATION

ENV CB_API_KEY_PROD ${CB_API_KEY_PROD}
ENV BUCKET_DESTINATION ${BUCKET_DESTINATION}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
ENTRYPOINT [ "python", "/app.py"]