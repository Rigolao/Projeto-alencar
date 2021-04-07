from django import forms
from .models import Documento, EDocModel, Pasta

class DocForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = ('title', 'description', 'tipo')

class UploadDocForm(forms.ModelForm):
    
    class Meta:
        model = EDocModel
        fields = ('title', 'pdf')   

class PastaForm(forms.ModelForm):

    class Meta:
        model = Pasta
        fields = ('title',)