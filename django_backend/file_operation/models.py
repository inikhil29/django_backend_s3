from django.db import models
from django.utils import timezone

class FileUploadModel(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255, default='')
    status = models.IntegerField(choices=[(0, 'Not Uploaded'), (1, 'Uploaded')], default=0)
    creation_timestamp = models.DateTimeField(default=timezone.now)


class UploadedFileDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    upload_file_id = models.ForeignKey(FileUploadModel, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    creation_timestamp = models.DateTimeField(default=timezone.now)