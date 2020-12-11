from django.conf.urls import url, include

from apps.ingreso.views import RegistroUsuario
    
# Acá se ponen las urls de la app, en este caso esta url es para registrar un nuevo usuario
urlpatterns= [
    url(r'nuevo', RegistroUsuario.as_view(),name='Registrar'),
]