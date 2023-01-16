import boto3


class S3Uploader:
    def __init__(self, bucket):
        self.bucket = bucket

    def clear_bucket(self):
        """
        Clear bucket contents before reloading
        """
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucket)
        response = bucket.objects.filter(Prefix="cb_org/").delete()
        return response

    def upload_fileobj(self, data, object_name):
        """
        Function to upload a file to an S3 bucket
        """

        s3_client = boto3.client('s3')
        response = s3_client.upload_fileobj(data, self.bucket, object_name)

        return response

    def upload_file(self, filename, object_name):
        """
        Function to upload a file to an S3 bucket
        """

        s3_client = boto3.client('s3')
        response = s3_client.upload_file(filename, self.bucket, object_name)

        return response

    def put_object(self, obj, object_name):
        """
        Function to upload a file to an S3 bucket
        """

        s3_client = boto3.client('s3')
        response = s3_client.put_object(Body=obj,
                                        Bucket=self.bucket,
                                        Key=object_name)

        return response
