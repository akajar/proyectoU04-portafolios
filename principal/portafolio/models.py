from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField()
    nombre = models.TextField()
    password = models.TextField() #ocultar
    foto_url = models.CharField(max_length=255)
    #timestamps
    created_at = models.DateTimeField(editable=False)
    done_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self) -> str:
        return self.nombre
class Proyecto(models.Model):
    foto_archivo = models.FileField()
    foto_url = models.URLField()
    titulo = models.TextField()
    descripcion = models.TextField()
    #tags = models.TextChoices()
    url = models.URLField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #timestamps
    created_at = models.DateTimeField(editable=False)
    done_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.titulo