from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UploadFileSerializer
from .models import FileUploadModel
from rest_framework import generics
# Create your views here.
class FileUploadView(APIView):
    def post(self, request, format=None):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            file_data = serializer.save()
            return Response({'message': 'File uploaded successfully.', 'success': True})
        return Response(serializer.errors, status=400)
    
class FileListAPIView(generics.ListAPIView):
    queryset = FileUploadModel.objects.all()
    serializer_class = UploadFileSerializer