import os
from crunchbase_extract import CrunchbaseExtractor
from boto3s3 import S3Uploader
import cProfile

CB_API_KEY = os.environ['CB_API_KEY_PROD']
BUCKET = os.environ['BUCKET_DESTINATION']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_PROD']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY_PROD']


def pageIterator(cbextractor, s3uploader, page_lim = 9999):
    page_no = 0
    api_selector = cbextractor.callAPI()
    for page in api_selector.iterate():
        if page_lim <= page_no:
            break
        page_no += 1
        s3uploader.put_object(cbextractor.jsonOutput(page), cbextractor.objectNamer(page_no))

def main():
    cbextractor = CrunchbaseExtractor(CB_API_KEY)
    s3uploader = S3Uploader(AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET)
    pageIterator(cbextractor, s3uploader, 5)

main()
#cProfile.run('main()')