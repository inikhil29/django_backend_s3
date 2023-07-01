from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.FileUploadView.as_view(), name="upload_file"),
    path('get_files/', views.FileListAPIView.as_view(), name="file_list"),
    path('get_files/<int:pk>/', views.GetFileDetails.as_view(), name='file_details')
]