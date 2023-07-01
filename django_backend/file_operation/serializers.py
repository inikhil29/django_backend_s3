# File: serializers.py
from rest_framework import serializers
from .models import FileUploadModel, UploadedFileDetailsModel
from services.s3_connection import S3Connection


class GetFileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = ['file_name', 'status', 'creation_timestamp']


class GetUploadedFileDetailsSerializer(serializers.ModelSerializer):
    upload_file = GetFileDetailsSerializer()

    class Meta: 
        model = UploadedFileDetailsModel
        fields = '__all__'

class UploadedFileDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UploadedFileDetailsModel
        fields = ["upload_file", "file_path"]


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
                'upload_file': upload_file_id
            }
            uploaded_file_serilizer = UploadedFileDetailsSerializer(data=uploaded_file_serilizer_data)
            if uploaded_file_serilizer.is_valid():
                uploaded_file_serilizer.save()
                file_upload_model.status = 1
                file_upload_model.save()
                return {'success': True}
            else:
                return {'errors': uploaded_file_serilizer.errors, 'success': False}    
        else:  
            return {'errors': 'Something went wrong while uploading file.', 'success': False}

    class Meta:
        model = FileUploadModel
        fields = "__all__"


class GetFileDetailsSerializer(serializers.ModelSerializer):
    upload_file = GetFileDetailsSerializer()
    file_url = serializers.SerializerMethodField()
    class Meta:
        model = UploadedFileDetailsModel
        fields = ['id', 'upload_file', 'file_path', 'creation_timestamp', 'file_url']

        
    def get_file_url(self, obj):
        s3Client = S3Connection()
        url = s3Client.get_url_of_obj(obj_name=obj.file_path)
        return url if url != False else ''