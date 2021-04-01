from django import forms
from .models import Documento

class DocForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = ('title', 'description', 'done')