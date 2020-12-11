from django.conf.urls import url, include

from apps.usuario.views import UsuarioList,UsuarioUpdate,UsuarioDelete, UsuarioCreate
    

#URLS de la aplicación
urlpatterns= [

    url(r'usuario', UsuarioCreate.as_view(),name='usuario_crear'),
    url(r'listar', UsuarioList.as_view(),name='usuario_listar'),
    url(r'editar/(?P<pk>\d+)/',UsuarioUpdate.as_view(),name='usuario_edit'),
    url(r'eliminar/(?P<pk>\d+)/', UsuarioDelete.as_view(),name='usuario_delete'),

]