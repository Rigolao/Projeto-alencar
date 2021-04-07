from django.contrib import admin

from .models import Documento
from .models import EDocModel
from .models import Pasta

admin.site.register(Documento)
admin.site.register(EDocModel)
admin.site.register(Pasta)