from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = CharField(max_length=100)
    descripcion = models.TextField()
    imagen = ImageField(upload_to='blog/images/')
    date = models.DateField(default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class archivo(models.Model):
    titulo = CharField(max_length=100)
    document = models.FileField(upload_to='documentos/')