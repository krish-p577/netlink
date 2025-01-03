# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new
from . import views 
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
]
