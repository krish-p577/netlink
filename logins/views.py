from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"







'''
# Create your views here.
def links(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
'''