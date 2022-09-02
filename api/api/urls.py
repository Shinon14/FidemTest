
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from quickstart.views import SolicitudGet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.groupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),                
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # aqui voy a crear un path para un metodo GET 
    path('api/solicitud/', SolicitudGet.as_view()),
    # aqui voy a crear un path para un metodo POST y generacion del pdf
    path('api/generarPdf/', views.GenerarPdf.as_view()),
    # url para generar el pdf con el nombre que se le pase por el body
    path('api/generarPdf/<pdf_name>', views.GenerarPdf.as_view()),
    
]