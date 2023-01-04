import json
import os

import boto3

from botocore.client import ClientError




class S3Uploader():
    def __init__(self,
                 aws_access_key,
                 aws_secret_key,
                 bucket):
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket = bucket

    def upload_fileobj(self, data,object_name):
        """
        Function to upload a file to an S3 bucket
        """

        s3_client = boto3.client('s3',
                                 aws_access_key_id=self.aws_secret_key,
                                 aws_secret_access_key=self.aws_access_key)
        response = s3_client.upload_fileobj(data, self.bucket, object_name)

        return response
