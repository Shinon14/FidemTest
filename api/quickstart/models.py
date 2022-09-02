from pyexpat import model
from django.db import models

# modelo de solicitud para la base de datos 

class Solicitud(models.Model):
    nroSolicitud = models.IntegerField()

    def __str__(self):
        return self.nroSolicitud


# modelo para el nombre del pdf que se va a generar

class PdfRequest (models.Model):
    pdf_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pdf_name
