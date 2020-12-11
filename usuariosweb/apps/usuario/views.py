from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.usuario.forms import UsuariosForm
from apps.usuario.models import usuarios

from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

# una clase para listar
class UsuarioList(ListView):
    model=usuarios
    template_name='tablas/tablas_list.html'
    success_url = reverse_lazy('usuario_listar')

# una clase para crear
class UsuarioCreate(CreateView):
    model=usuarios
    form_class=UsuariosForm
    template_name='tablas/tablas_form.html'
    success_url = reverse_lazy('usuario_listar')

# una clase para actualizar o editar
class UsuarioUpdate(UpdateView):
    model=usuarios
    form_class=UsuariosForm
    template_name='tablas/tablas_form.html'
    success_url = reverse_lazy('usuario_listar')

# una clase para borrar
class UsuarioDelete(DeleteView):
    model=usuarios
    form_class=UsuariosForm
    template_name='tablas/tablas_delete.html'
    success_url = reverse_lazy('usuario_listar')
