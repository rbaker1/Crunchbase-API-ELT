import os
import logging
from crunchbase_extract import CrunchbaseExtractor
from boto3s3 import S3Uploader

CB_API_KEY = os.environ['CB_API_KEY_PROD']
BUCKET = os.environ['BUCKET_DESTINATION']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def pageIterator(cbextractor, s3uploader, page_lim=9999):
    page_no = 0
    api_selector = cbextractor.callAPI()
    for page in api_selector.iterate():
        if page_lim <= page_no:
            break
        page_no += 1
        try:
            s3uploader.put_object(cbextractor.extractionOutput(page, 'json'), cbextractor.objectNamer(page_no))
            print('Successfully extracted and uploaded page ' + str(page_no))
        except Exception:
            raise Exception('Unable to upload to s3. Job failed on page ' + str(page_no))


def main():
    cbextractor = CrunchbaseExtractor(CB_API_KEY)
    s3uploader = S3Uploader(BUCKET)
    s3uploader.clear_bucket()
    pageIterator(cbextractor, s3uploader)

main()
