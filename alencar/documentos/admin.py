from django.contrib import admin

from .models import Documento
from .models import EDocModel

admin.site.register(Documento)
admin.site.register(EDocModel)