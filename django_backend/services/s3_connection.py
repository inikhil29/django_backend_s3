import boto3
from django.conf import settings
from botocore.exceptions import NoCredentialsError


class S3Connection():
    bucket_name_default = settings.AWS_STORAGE_BUCKET_NAME
    def __init__(self) -> None:
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        
    def upload_file(self, file, bucket_name = '', file_path = 'default/'):
        try:
            bucket_name = self.bucket_name_default
            self.s3_client.upload_fileobj(file, bucket_name, file_path)
            return True 
        except NoCredentialsError:
            return False
