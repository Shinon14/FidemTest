from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions 
from quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.models import Solicitud
from quickstart.serializers import SolicitudSerializer
from quickstart.serializers import PdfRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


from rest_framework import generics


# clase para los usuarios default de django


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# clase para los grupos defaul de django

class groupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



 # esta clase es para el metodo get en el que si es mayor a 3 devuelve un mensaje de error para 
class SolicitudGet(generics.ListCreateAPIView):
    serializer_class = SolicitudSerializer
    def get(self, request, *args, **kwargs):
        if Solicitud.objects.count() < 3:
            return self.list(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
            


# esta clase es para el metodo post y generar un pdf con el nombre que se le pase por el body

class GenerarPdf(APIView):
    # llamo al serializador para que me devuelva el nombre del pdf
    serializer_class = PdfRequestSerializer
    # defino el metodo post
    def post(self, request, *args, **kwargs):
        # creo un objeto de tipo serializador y le paso el request
        pdf_name = request.data['pdf_name']
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        # aqui creo el pdf, le doy las medidas y el nombre como parametro, para despues guardarlo
        p.drawString(500, 250, pdf_name)
        p.showPage()
        p.save()
        buffer.seek(0)
        # devuelvo el pdf y lo transforma en un archivo descargable desde el navegador, con el nombre que le pase por el body
        return FileResponse(buffer, as_attachment=True, filename=pdf_name+'.pdf')