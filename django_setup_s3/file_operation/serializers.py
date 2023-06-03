# File: serializers.py
from rest_framework import serializers
from .models import FileUploadModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = ('file',)