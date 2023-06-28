from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UploadFileSerializer, UploadedFileDetailsSerializer
from .models import FileUploadModel, UploadedFileDetailsModel
from rest_framework import generics
# Create your views here.
class FileUploadView(APIView):
    def post(self, request, format=None):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            file_data = serializer.save()
            return Response({'message': 'File uploaded successfully.', 'success': True}, status=200)
        return Response({'error': serializer.errors, 'success': False}, status=400)
    
class FileListAPIView(generics.ListAPIView):
    queryset = UploadedFileDetailsModel.objects.all()
    serializer_class = UploadedFileDetailsSerializer
    print('-------------------------->')
    print(queryset)
    print('-------------------------->')
    print(serializer_class)
    print('-------------------------->')