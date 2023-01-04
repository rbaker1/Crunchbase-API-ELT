import os
from crunchbase_extract import CrunchbaseExtractor
from boto3s3 import S3Uploader
import cProfile

"""CB_API_KEY = os.environ['CB_API_KEY_PROD']
BUCKET = os.environ['BUCKET_DESTINATION']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_PROD']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY_PROD']"""

CB_API_KEY = '82a47b7c8d83a0695baeb7ed00659c0c'
BUCKET = 'hubilo-crunchbase-api-extract-dev'
AWS_ACCESS_KEY = 'AKIA2VPSUKHMZYRYEUUZ'
AWS_SECRET_KEY = 'rDLsKvrOtuS0cfnWqB0hcUwpRw40vLk9qrvcSu3'
def main():
    cbextractor = CrunchbaseExtractor(CB_API_KEY)
    s3uploader = S3Uploader(AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET)
    data, objectname = cbextractor.callAPI()

    #return data

    return s3uploader.upload_fileobj(data, objectname)

#main()
cProfile.run('main()')