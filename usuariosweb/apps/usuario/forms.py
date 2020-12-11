from django import forms
from apps.usuario.models import usuarios

# Crear formularios
class UsuariosForm(forms.ModelForm):
    class Meta:
        model= usuarios

            
        fields = [  
            'usuario',
            'nombrecompleto',
            'correo',
            'contraseña',
            'documento',
            'telefono',
        ]
        labels = {
            'usuario': 'Usuario',
            'nombrecompleto': 'Nombre Completo',
            'correo':'Correo Electrónico',
            'contraseña':'Contraseña',
            'documento':'Documento de Identidad',
            'telefono':'Teléfono',     
        }
        widgets ={
            'usuario':forms.TextInput(attrs={'class':'form-control'}),
            'nombrecompleto':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'contraseña':forms.TextInput(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),   
        }