from django.db import models
from django.contrib.auth import get_user_model

class Documento(models.Model):

    STATUS = (
        ('done', 'Empresa'),
        ('doing', 'Assunto'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf = models.FileField(upload_to='upload_pdf/', max_length=100, blank=True)
    tipo = models.CharField(
        max_length=7,
        choices=STATUS
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

