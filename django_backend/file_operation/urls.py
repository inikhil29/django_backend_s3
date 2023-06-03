from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.FileUploadView.as_view(), name="upload_file")
]