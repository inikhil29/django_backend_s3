from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyModelSerializer
# Create your views here.

def upload_file(request):
    return HttpResponse('Test Hello')


class FileUploadView(APIView):
    def post(self, request, format=None):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'File uploaded successfully.'})
        return Response(serializer.errors, status=400)