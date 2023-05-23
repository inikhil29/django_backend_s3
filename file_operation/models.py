from django.db import models

# Create your models here.

from django.db import models

class FileUploadModel(models.Model):
    file = models.FileField(upload_to='uploads/')
