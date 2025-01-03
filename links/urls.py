from django.urls import path
from . import views 

urlpatterns = [
    path('links/', views.links, name = 'links'),
    path('links/<int:id>/', views.dynamic_links, name='dynamiclinks')
]