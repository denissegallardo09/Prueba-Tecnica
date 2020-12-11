from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.ingreso.forms import RegistroForm

# Se crea función de vista mendiante la importación de los formularios creados
class RegistroUsuario(CreateView):
    models = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuario_listar')