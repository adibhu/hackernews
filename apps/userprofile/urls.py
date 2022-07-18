from django.urls import path
from .views import userprofile

urlpattens = [
    path('<str:username>/', userprofile, name='userprofile'),
]