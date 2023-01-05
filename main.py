import os
from crunchbase_extract import CrunchbaseExtractor
from boto3s3 import S3Uploader
import cProfile

CB_API_KEY = os.environ['CB_API_KEY_PROD']
BUCKET = os.environ['BUCKET_DESTINATION']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_PROD']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY_PROD']


def main():
    cbextractor = CrunchbaseExtractor(CB_API_KEY)
    s3uploader = S3Uploader(AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET)
    data, objectname = cbextractor.callAPI()
    #return data

    #return s3uploader.upload_file(cbextractor.writeOutput(data, objectname), objectname)
    return s3uploader.put_object(data, objectname)

#main()
cProfile.run('main()')