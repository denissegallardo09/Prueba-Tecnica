from django.contrib import admin

# Register your models here.
from apps.usuario.models import usuarios


admin.site.register(usuarios)