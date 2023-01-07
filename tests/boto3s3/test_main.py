import random
from unittest.mock import patch, MagicMock

import pytest

from ...boto3s3 import S3Uploader

class TestS3Uploader:
    @pytest.fixture(name='s3', scope='class')
    def s3_instance(self):
        return S3Uploader('key')

    def test_init(self):
        s3 = S3Uploader('aws_access_key',
                         'aws_secret_key',
                         'bucket')
        assert s3.aws_access_key == 'aws_access_key'
        assert s3.aws_secret_key == 'aws_secret_key'
        assert s3.bucket == 'bucket'

        s3 = S3Uploader()
        assert s3.aws_access_key is None
        assert s3.aws_secret_key is None
        assert s3.bucket is None