from django.urls import path

from . import views

urlpatterns = [
    path('', views.empresaHome, name="empresa-home"),
    path('doc/', views.empresaDoc, name="empresa-doc"),
    path('documento/<int:id>', views.documentoView, name="documento-view"),
]
