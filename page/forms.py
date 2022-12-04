from django import forms
from .models import cars

class ComplaintForm(forms.ModelForm):
    class Meta:
        model= cars
        fields=('__all__')
            
            
        
