from django import forms
from .models import Documento, EDocModel

class DocForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = ('title', 'description', 'tipo')

class UploadDocForm(forms.ModelForm):
    
    class Meta:
        model = EDocModel
        fields = ('title', 'pdf')   