# File: serializers.py
from rest_framework import serializers
from .models import FileUploadModel, UploadedFileDetailsModel
from services.s3_connection import S3Connection


class UploadedFileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFileDetailsModel
        fields = "__all__"


class UploadFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    file_name = serializers.CharField(required=False)
    def create(self, validated_data):
        file = validated_data["file"]
        file_upload_model = FileUploadModel(file_name=file.name)
        file_upload_model.save()
        upload_file_id = file_upload_model.id
        file_name = file_upload_model.file_name
        s3Client = S3Connection()
        file_upload_res = s3Client.upload_file(file, bucket_name='', file_path=f"upload/{upload_file_id}/{file_name}")
        if file_upload_res: 
            uploaded_file_serilizer_data = {
                'file_path' : f"upload/{upload_file_id}/{file_name}",
                'upload_file_id': upload_file_id
            }
            file_upload_model.status = 1
            file_upload_model.save()
            uploaded_file_serilizer = UploadedFileDetailsSerializer(data=uploaded_file_serilizer_data)
            if uploaded_file_serilizer.is_valid():
                uploaded_file_serilizer.save()
            return True
        else:  
            return False

    class Meta:
        model = FileUploadModel
        fields = "__all__"
