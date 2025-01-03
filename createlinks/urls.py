from django.urls import path
from . import views 

urlpatterns = [
    path('create/', views.createlinks, name = 'create'),
]