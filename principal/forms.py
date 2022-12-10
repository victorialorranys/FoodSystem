from django import forms
from principal.models import *

class ClienteForm(forms.ModelForm):
 
    class Meta:
        model= Cliente
        fields = '__all__'
