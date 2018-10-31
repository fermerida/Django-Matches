# -*- coding: utf-8 -*-
from django import forms
import cx_Oracle 

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


rol_choice= [
    ('1', 'Administrador'),
    ('2', 'Empleado'),
    ('3', 'Cliente'),
    ('4', 'Usuario Congelado'),

    ]


gender_choice= [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ]

more_choice= [
    ('0', 'Menos'),
    ('1', 'Mas'),
    ]

member_choice= [
    ('0', 'Sin Membresia'),
    ('1', 'Con Membresia'),
    ]

file_choice= [
    ('1', 'Estadios'),
    ('2', 'Directores'),
    ('3', 'Equipos'),
    ('4', 'Jugadores'),
    ('5', 'Competiciones'),
    ('6', 'Incidencias'),
    ]
game_choice= [
    ('1', 'Finalizado'),
    ('2', 'Sin Iniciar'),
    ('3', 'Suspendido'),
    ('4', 'En Curso'),
    ]

team_choice= [
    ('Real Madrid', 'Real Madrid'),
    ('Barcelona', 'Barcelona'),
    ('Chelsea', 'Chelsea'),
    ('Manchester United', 'Manchester United'),
    ('Arsenal', 'Arsenal'),
    ('Liverpool', 'Liverpool'),
    ('Valencia', 'Valencia'),
    ('Athletic Club', 'Athletic Club'),
    ]

class loginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class registroForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.CharField(widget=forms.TextInput,required=True)
    nombre = forms.CharField(widget=forms.TextInput,required=True)
    apellido = forms.CharField(widget=forms.TextInput,required=True)
    direccion = forms.CharField(widget=forms.TextInput,required=True)
    telefono = forms.CharField(widget=forms.TextInput,required=True)
    pais = forms.CharField(widget=forms.TextInput,required=True)
    genero= forms.CharField(label='Selecciona el genero:', widget=forms.Select(choices=gender_choice))
    birthday = forms.CharField(widget=forms.TextInput,required=True)
    foto = forms.CharField(widget=forms.TextInput,required=False)
    team= forms.CharField(label='Selecciona tu equipo favorito:', widget=forms.Select(choices=team_choice))

class crudadd(forms.Form):
        
    username = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.CharField(widget=forms.TextInput,required=True)
    nombre = forms.CharField(widget=forms.TextInput,required=True)
    apellido = forms.CharField(widget=forms.TextInput,required=True)
    direccion = forms.CharField(widget=forms.TextInput,required=True)
    telefono = forms.CharField(widget=forms.TextInput,required=True)
    pais = forms.CharField(widget=forms.TextInput,required=True)
    genero= forms.CharField(label='Selecciona el genero:', widget=forms.Select(choices=gender_choice))
    birthday = forms.CharField(widget=forms.TextInput,required=True)
    foto = forms.CharField(widget=forms.TextInput,required=False)
    team= forms.CharField(label='Selecciona subscripcion:', widget=forms.Select(choices=team_choice))
    rol= forms.CharField(label='Selecciona el Rol:', widget=forms.Select(choices=rol_choice))

class crudmod(forms.Form):
        
    username = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.CharField(widget=forms.TextInput,required=True)
    nombre = forms.CharField(widget=forms.TextInput,required=True)
    apellido = forms.CharField(widget=forms.TextInput,required=True)
    direccion = forms.CharField(widget=forms.TextInput,required=True)
    telefono = forms.CharField(widget=forms.TextInput,required=True)
    pais = forms.CharField(widget=forms.TextInput,required=True)
    genero= forms.CharField(label='Selecciona el genero:', widget=forms.Select(choices=gender_choice))
    birthday = forms.CharField(widget=forms.TextInput,required=True)
    foto = forms.CharField(widget=forms.TextInput,required=False)
    team= forms.CharField(label='Selecciona subscripcion:', widget=forms.Select(choices=team_choice))
    rol= forms.CharField(label='Selecciona el Rol:   ', widget=forms.Select(choices=rol_choice))    

class crudeliminar(forms.Form):
        
    username = forms.CharField(widget=forms.TextInput,required=True)
    
class crudfreeze(forms.Form):
        
    username = forms.CharField(widget=forms.TextInput,required=True)

class carga(forms.Form):
        
    url = forms.CharField(widget=forms.TextInput,required=True)
    option= forms.CharField(label='Selecciona el tipo de archivo:', widget=forms.Select(choices=file_choice))  

class rep1 (forms.Form):
    x = forms.CharField(label='Jugadores y tecnicos de equipo:', widget=forms.TextInput, required=True)     

class rep2 (forms.Form):
    x = forms.CharField(label='Jugadores y tecnicos mayores a:', widget=forms.TextInput, required=True)     

class rep3 (forms.Form):
    x = forms.CharField(label='Jugadores y tecnicos menores a:', widget=forms.TextInput, required=True)     

class rep4 (forms.Form):
    x = forms.CharField(label='Equipos participantes en competicion:', widget=forms.TextInput, required=True)     

class rep5 (forms.Form):
    x = forms.CharField(label='Equipos de país:', widget=forms.TextInput, required=True)     

class rep6 (forms.Form):
    x = forms.CharField(label='Equipos con antiguedad de(anos):', widget=forms.TextInput, required=True)     

class rep7 (forms.Form):
    x = forms.CharField(label='Estadios en país:', widget=forms.TextInput, required=True)     

class rep8 (forms.Form):
    x = forms.CharField(label='Estadios con capacidad menor o igual a:', widget=forms.TextInput, required=True)     

class rep9 (forms.Form):
    x = forms.CharField(label='Historico de partidos de equipo:', widget=forms.TextInput, required=True)     

class rep10 (forms.Form):
    x = forms.CharField(label='Equipos en los que ha estado o dirigido (Tecnico o Jugador):', widget=forms.TextInput, required=True)     

class rep11 (forms.Form):
    x = forms.CharField(label='Partidos donde hubo al menos cantidad de goles (Número de goles):', widget=forms.TextInput, required=True)     

class rep12 (forms.Form):
    x = forms.CharField(label='Incidencias:', widget=forms.TextInput, required=True)     
    y = forms.CharField(label='Competicion:', widget=forms.TextInput, required=True)     

class rep13(forms.Form):
    x = forms.CharField(label='Incidencias:', widget=forms.TextInput, required=True)     
    y = forms.CharField(label='Competicion:', widget=forms.TextInput, required=True)     
    z = forms.CharField(label='Anio:', widget=forms.TextInput, required=True)     

class rep14 (forms.Form):
    x = forms.CharField(label='Competicion:', widget=forms.TextInput, required=True)     
    y = forms.CharField(label='Equipo ganador:', widget=forms.TextInput, required=True)     

class rep15 (forms.Form):
    x = forms.CharField(label='Partidos en Anio:', widget=forms.TextInput, required=True)     

class rep16 (forms.Form):
    x = forms.CharField(label='Equipo 1:', widget=forms.TextInput, required=True)     
    y = forms.CharField(label='Equipo 2:', widget=forms.TextInput, required=True)     

class rep17 (forms.Form):
    x = forms.CharField(label='Partidos de equipo:', widget=forms.TextInput, required=True)     

class clientg (forms.Form):
    x= forms.CharField(label='Selecciona el estado de partido:   ', widget=forms.Select(choices=game_choice))    

class arep1 (forms.Form):
    x = forms.CharField(label='Usuarios Suscritos a  equipo:', widget=forms.TextInput, required=True)     

class arep2 (forms.Form):
    x= forms.CharField(label='Selecciona el tipo de cliente:', widget=forms.Select(choices=member_choice))

class arep3 (forms.Form):
    x = forms.CharField(label='Jugadores y tecnicos menores a:', widget=forms.TextInput, required=True)     

class arep4 (forms.Form):
    x = forms.CharField(label='Usuarios de País:', widget=forms.TextInput, required=True)     

class arep5 (forms.Form):
    x = forms.CharField(label='Usuarios de País:', widget=forms.TextInput, required=True)     

class arep6 (forms.Form):
    x= forms.CharField(label='Selecciona el genero:', widget=forms.Select(choices=gender_choice))

class arep7 (forms.Form):
    x = forms.CharField(label='Usuarios con al menos edad de:', widget=forms.TextInput, required=True)     

class arep8 (forms.Form):
    x= forms.CharField(label='Selecciona una opcion:', widget=forms.Select(choices=more_choice))

class arep9 (forms.Form):
    x= forms.CharField(label='Selecciona una opcion:', widget=forms.Select(choices=more_choice))

class arep10 (forms.Form):
    x = forms.CharField(label='Equipos en los que ha estado o dirigido (Tecnico o Jugador):', widget=forms.TextInput, required=True)     
