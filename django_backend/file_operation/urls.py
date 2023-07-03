from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.FileUploadView.as_view(), name="upload-file"),
    path('get_files/', views.FileListAPIView.as_view(), name="file-list"),
    path('get_files/<int:pk>/', views.GetFileDetailsAPIView.as_view(), name='file-details'),
    path('delete_file/', views.DeleteFileAPIView.as_view(), name='delete-file' )
]