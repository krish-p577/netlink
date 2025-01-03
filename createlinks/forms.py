from django import forms
from .models import Linkset

# creating a form 

class LinkForm(forms.ModelForm):
    class Meta:
        model = Linkset
        fields = [
            'biography',
            'linkone',
            'defone',
            'linktwo',
            'deftwo',
            'linkthree',
            'defthree', 
            
        ]


    def clean_linktwo(self, *args, **kwargs):
        linktwo = self.cleaned_data.get('linktwo')
        if '.com' not in linktwo: # type: ignore
            raise forms.ValidationError('Please enter a valid website (Ending in .com)')
        return linktwo

    def clean_linkthree(self, *args, **kwargs):
        linkthree = self.cleaned_data.get('linkthree')
        if '.com' not in linkthree: # type: ignore
            raise forms.ValidationError('Please enter a valid website (Ending in .com)')
        return linkthree


    def clean_linkone(self, *args, **kwargs):
        linkone = self.cleaned_data.get('linkone')
        if '.com' not in linkone: # type: ignore
            raise forms.ValidationError('Please enter a valid website (Ending in .com)')
        return linkone
'''
    def send_user(self, *args, **kargs):
        return Linkset.user
'''
