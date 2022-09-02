# importaciones de django para los modelos y serializadores

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Solicitud
from quickstart.models import PdfRequest


# Serializers de django para los modelos de usuario y grupo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# Serializers para el modelo de solicitud 
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['nroSolicitud']


# Serializador para el nombre del pdf que se va a generar

class PdfRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfRequest
        fields = ['pdf_name']