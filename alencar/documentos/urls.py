from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.empresaHome, name="empresa-home"),
    path('doc/', views.empresaDoc, name="empresa-doc"),
    path('documento/<int:id>', views.documentoView, name="documento-view"),
    # path('novodoc/', views.novoDoc, name="novo-doc"),
    path('edit/<int:id>', views.editDoc, name="edit-doc"),
    path('delete/<int:id>', views.deleteDoc, name="delete-doc"),
    path('doc/upload', views.DocUploadView, name="DocUploadView"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
