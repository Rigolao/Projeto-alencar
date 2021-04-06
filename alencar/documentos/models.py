from django.db import models
from django.contrib.auth import get_user_model

class Documento(models.Model):

    STATUS = (
        ('done', 'Empresa'),
        ('doing', 'Assunto'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    tipo = models.CharField(
        max_length=7,
        choices=STATUS
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class EDocModel(models.Model):

    title = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

