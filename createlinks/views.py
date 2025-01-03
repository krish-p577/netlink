from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LinkForm

#creating an html form will allow changing the name of the 
# fields when entering information on the website 
def createlinks(request):
    form = LinkForm(request.POST or None)
    user = request.user

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        form = LinkForm()
    context = {
        'form' : form, 
        'user' : user
        
    }
    return render(request, 'makelinks.html', context)
    







#hello krish, rn you need to work on form validation okay 




