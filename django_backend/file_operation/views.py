from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UploadFileSerializer, UploadedFileDetailsSerializer, GetUploadedFileDetailsSerializer, GetFileDetailsSerializer
from .models import FileUploadModel, UploadedFileDetailsModel
from rest_framework import generics
# Create your views here.

#View for File Uplaod
class FileUploadView(APIView):
    def post(self, request, format=None):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            file_data = serializer.save()
            if file_data.get('success', False) == True:
                return Response({'message': 'File uploaded successfully.', 'success': True}, status=200)
            else:
                if file_data.get('errors', False):
                    return Response({'error': file_data.get('errors', ''), 'success': False}, status=400)
                else:
                    return Response({'error': 'Something Went Wrong!!!', 'success': False}, status=400)
        else:
            return Response({'error': serializer.errors, 'success': False}, status=400)
    
#View for get the uploaded file list
class FileListAPIView(generics.ListAPIView):
    queryset = UploadedFileDetailsModel.objects.select_related('upload_file')
    serializer_class = GetUploadedFileDetailsSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        status_code = 200
        return Response(data, status=status_code)

#view for get a file details
class GetFileDetails(generics.RetrieveAPIView):
    queryset = UploadedFileDetailsModel.objects.select_related('upload_file')
    serializer_class = GetFileDetailsSerializer

