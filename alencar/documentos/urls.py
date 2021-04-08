from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.pastaList, name="pasta-list"),
    path('pasta/<int:id>', views.pastaView, name="pasta-view"),
    path('novapasta/', views.novaPasta, name="nova-pasta"),
    path('delete/<int:id>', views.deletePasta, name="delete-pasta"),
    # path('pasta/<int:id>/itens', views.itensList, name="itens-list"),
    path('doc/', views.empresaDoc, name="empresa-doc"),
    path('documento/<int:id>', views.documentoView, name="documento-view"),
    # path('novodoc/', views.novoDoc, name="novo-doc"),
    path('edit/<int:id>', views.editDoc, name="edit-doc"),
    path('delete/<int:id>', views.deleteDoc, name="delete-doc"),
    #path('doc/upload', views.DocUploadView, name="DocUploadView"),
    path('pasta/<int:id>/upload', views.DocUploadView, name="DocUploadView"),
    #path('pasta/<int:id>/delete/<int:id>', views.deleteItem, name="delete-item"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
