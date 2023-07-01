import boto3
from django.conf import settings
from botocore.exceptions import NoCredentialsError
from django.core.files.storage import default_storage


class S3Connection():
    bucket_name_default = settings.AWS_STORAGE_BUCKET_NAME
    def __init__(self) -> None:
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        
    def upload_file(self, file, bucket_name = '', file_path = 'default/'):
        try:
            bucket_name = self.bucket_name_default if bucket_name == '' else bucket_name
            self.s3_client.upload_fileobj(file, bucket_name, file_path)
            return True 
        except NoCredentialsError:
            return False

    def get_url_of_obj(self, obj_name, bucket_name=''):
        try:
            bucket_name = self.bucket_name_default if bucket_name == '' else bucket_name
            s3_base_url = self.get_s3_base_url()

            url = self.s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket_name, 'Key': obj_name},
                                                        ExpiresIn=3600)
            if url:
                return url
            return False
        except NoCredentialsError:
            return False
        

    def get_s3_base_url(self, bucket_name=''):
        try:
            bucket_name = self.bucket_name_default if bucket_name == '' else bucket_name
            response = self.s3_client.get_bucket_location(Bucket=bucket_name)
            bucket_location = response['LocationConstraint']
            s3_base_url = f"https://s3-{bucket_location}.amazonaws.com/{bucket_name}"
            return s3_base_url
        except NoCredentialsError:
            return False
        
    def get_s3_bucket_location(self, bucket_name):
        try:
            bucket_name = self.bucket_name_default if bucket_name == '' else bucket_name
            response = self.s3_client.get_bucket_location(Bucket=bucket_name)
            bucket_location = response['LocationConstraint']
            return bucket_location if bucket_location else False
        except NoCredentialsError:
            return False