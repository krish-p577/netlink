from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from createlinks.models import Linkset
def links(request):
    objs = Linkset.objects.all()
    context = {
        'more' : objs,
    }
    return render(request, "linkpage.html", context)

def dynamic_links(request, id):
    obj = Linkset.objects.get(id = id)
    context = {
        'obj' : obj
    }
    return render(request, 'userlinks.html', context)


    
    
