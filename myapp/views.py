# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect	
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.core.mail import send_mail

import os
import csv
import subprocess
import cx_Oracle
import datetime
import sys

# Create your views here.
from myapp.forms import loginForm, carga, registroForm, clientg, crudadd, crudfreeze, crudmod, crudeliminar, rep1, rep2,rep3, rep4, rep5, rep6, rep7, rep8, rep9, rep10, rep11, rep12, rep13, rep14, rep15, rep16, rep17, arep1, arep2,arep3, arep4, arep5, arep6, arep7, arep8, arep9, arep10

def index(request):
    return render(request, 'index.html')


def login(request):
    # This view is missing all form handling logic for simplicity of the example
    form = loginForm(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():
        subject = 'Yellow Footbal - acceptance Mail'
        from_email = 'fer.merida94@gmail.com'
        to_email =['fer.merida94@gmail.com']
        contact_message= 'Welcome to our app'
        some_html_message = render_to_string('mail.html', {'varname':'value'})
        send_mail(subject, contact_message, from_email, to_email,html_message =some_html_message, fail_silently=False)
        datos = form.cleaned_data
        user = datos.get("usuario")
        psw = datos.get("password")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        cursor.execute('select USUARIO, CLAVE, TIPO from USUARIO')
        for row in cursor:     
            print >>sys.stderr, row[2]     
            if user == row[0] and psw == row[1]:
                print >>sys.stderr, 'logged'   
                #usuario = auth.authenticate(username = user, password = psw)
                #auth.login(request, usuario)
                if row[2]== 1:
                    return render(request, 'administrador.html', {'user': user})
                elif row[2]== 2:
                    return render(request, 'empleado.html', {'user': user})
                elif row[2]== 3:
                    return render(request, 'cliente.html', {'user': user})
                   #return render(request, 'clienteme.html', {'user': user})
                elif row[2]== 4:
                    return render(request, 'frozen.html', {'user': user})
                else:
                    return render(request, 'frozen.html', {'user': user})

    return render(request, 'login.html', {'form': loginForm()})

def administrar(request):
    return render(request, 'administrador.html')

def cliente(request):
    form = clientg(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        opcion = 'Finalizado'
        if x== '1':
            opcion = 'Finalizado'
        elif x== '2':
            opcion = 'Sin Iniciar'
        elif x== '3':
            opcion = 'Suspendido'
        elif x== '4':
            opcion = 'En Curso'

        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION, max(incidencia.Marcador) from partido, incidencia where partido.Estadio = incidencia.Estadio and partido.fecha = incidencia.fecha and partido.estado= \'' + opcion + '\' Group by partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION' 
        cursor.execute(statement)
        return render(request, 'cliente.html',{'result': cursor.fetchall(), form:clientg()})
    return render(request, 'cliente.html',{'form': clientg()})

def clientem(request):
    form = clientg(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        opcion = 'Finalizado'
        if x== '1':
            opcion = 'Finalizado'
        elif x== '2':
            opcion = 'Sin Iniciar'
        elif x== '3':
            opcion = 'Suspendido'
        elif x== '4':
            opcion = 'En Curso'

        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION, max(incidencia.Marcador) from partido, incidencia where partido.Estadio = incidencia.Estadio and partido.fecha = incidencia.fecha and partido.estado= \'' + opcion + '\' Group by partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION' 
        cursor.execute(statement)
        return render(request, 'clienteme.html',{'result': cursor.fetchall(), form:clientg()})
    return render(request, 'clienteme.html',{'form': clientg()})

def frozen(request):
    return render(request, 'frozen.html')
def empleado(request):
    return render(request, 'empleado.html')


def registro(request):
    form = registroForm(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")
        contra = datos.get("password")
        mail = datos.get("email")
        nombre = datos.get("nombre")
        apellido = datos.get("apellido")
        genero = datos.get("genero")
        telefono = datos.get("telefono")
        direccion = datos.get("direccion")
        fecha_registro = datetime.date.today()
        birthday = datos.get("birthday")
        pais = datos.get("pais")
        photo = datos.get("foto")        
        rol = 4
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        subject = 'Yellow Footbal - acceptance Mail'
        from_email = 'fer.merida94@gmail.com'
        to_email =[mail]
        contact_message= 'Welcome to our app'
        send_mail(subject, contact_message, from_email, to_email,fail_silently=False)

        if photo == "":
            blobvar = None
        else:
            file = open (photo,'rb')
            ext = 'jpg'
            content = file.read()
            file.close()
            blobvar = cursor.var(cx_Oracle.BLOB)
            blobvar.setvalue(0,content)

        statement2 = 'insert into usuario(NOMBRES, APELLIDOS, CLAVE, CORREO, TELEFONO, GENERO, FECHA_NACIMIENTO, FECHA_REGISTRO,DIRECCION, PAIS,TIPO, FOTO, USUARIO) values(:2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)'
        cursor.execute(statement2, (nombre, apellido, contra, mail, telefono, genero, birthday, fecha_registro, direccion, pais, rol, blobvar, usuario))
        connection.commit()
        return render(request, 'clientes.html', {'form': registroForm()})
    return render(request, 'registro.html', {'form': registroForm()})

def success(request):
        rol = 3
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement2 = 'UPDATE usuario SET tipo = 3 where usuario.usuario = \'' + 'andy' +'\''
        cursor.execute(statement2)
        connection.commit()
        return render(request, 'success.html')

def crud_agregar(request):
    form = crudadd(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")
        contra = datos.get("password")
        mail = datos.get("email")
        nombre = datos.get("nombre")
        apellido = datos.get("apellido")
        genero = datos.get("genero")
        telefono = datos.get("telefono")
        direccion = datos.get("direccion")
        fecha_registro = datetime.date.today()
        birthday = datos.get("birthday")
        pais = datos.get("pais")
        photo = datos.get("foto")        
        rol = datos.get("rol")      
            
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        if photo == "":
            blobvar = None
        else:
            file = open (photo,'rb')
            ext = 'jpg'
            content = file.read()
            file.close()
            blobvar = cursor.var(cx_Oracle.BLOB)
            blobvar.setvalue(0,content)
        statement2 = 'insert into usuario(NOMBRES, APELLIDOS, CLAVE, CORREO, TELEFONO, GENERO, FECHA_NACIMIENTO, FECHA_REGISTRO,DIRECCION, PAIS,TIPO, FOTO, USUARIO) values(:2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)'
        cursor.execute(statement2, (nombre, apellido, contra, mail, telefono, genero, birthday, fecha_registro, direccion, pais, rol, blobvar, usuario))
        connection.commit()
        return render(request, 'administrador.html', {'form': crudadd()})
    return render(request, 'crud_agregar.html', {'form': crudadd()})


def crud_mod(request):
    form = crudmod(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")
        contra = datos.get("password")
        mail = datos.get("email")
        nombre = datos.get("nombre")
        apellido = datos.get("apellido")
        genero = datos.get("genero")
        telefono = datos.get("telefono")
        direccion = datos.get("direccion")
        fecha_registro = datetime.date.today()
        birthday = datos.get("birthday")
        pais = datos.get("pais")
        photo = datos.get("foto")        
        rol = datos.get("rol")      
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        
        if photo == "":
            blobvar = None
        else:
            file = open (photo,'rb')
            ext = 'jpg'
            content = file.read()
            file.close()
            blobvar = cursor.var(cx_Oracle.BLOB)
            blobvar.setvalue(0,content)
        statement = 'update USUARIO SET nombres=\'' + nombre +'\', apellidos= \''+ apellido+ '\', clave=\''+ contra+ '\', correo=\''+ mail+ '\', telefono=\''+ telefono+ '\', genero=\''+ genero+ '\', fecha_nacimiento=\''+ birthday+ '\', direccion=\''+ direccion+ '\', pais=\''+ pais+ '\', tipo='+ tipo+ ' where usuario = \'' + usuario+ '\'' 
        cursor.execute(statement)
        connection.commit()
        return render(request, 'administrador.html', {'form': crudmod()})
    return render(request, 'crud_modificar.html', {'form': crudmod()})





def crud_eliminar(request):
    form = crudeliminar(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")
        print >>sys.stderr, usuario

        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'delete from usuario where usuario= '
        statement2 = statement + '\''  + usuario +'\''
        print >>sys.stderr, statement2
        cursor.execute(statement2)
        connection.commit()
        return render(request, 'administrador.html', {'form': crudeliminar()})
    return render(request, 'crud_eliminar.html', {'form': crudeliminar()})



def crud_congelar(request):
    form = crudeliminar(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")

        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'update USUARIO SET rol= 5 where usuario = \'' + usuario+ '\'' 
        cursor.execute(statement)
        connection.commit()
        return render(request, 'administrador.html', {'form': crudfreeze()})
    return render(request, 'crud_congelar.html', {'form': crudfreeze()})



def carga_mas(request):
    form = carga(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        url = datos.get("url")
        option = datos.get("option")
        
        f = open(url)
        csv_f = csv.reader(f, delimiter=str(u';').encode('utf-8'))
        next(csv_f, None)
        if option == 1:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into estadio(nombre, pais, fecha_open, capacidad, direccion, estado) values(\'' + row[1]+ '\',\'' + row[0]+ '\',\'' + row[2]+ '\',\'' + row[3]+ '\',\'' + row[4]+ '\',\'' + row[5]+'\')'
                cursor.execute(statement)
                connection.commit()
        elif option == 2:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into tecnico(nombre, fecha_nac, pais, estado) values(\'' + row[0]+ '\',\'' + row[1]+ '\',\'' + row[2]+ '\',\'' + row[3]+'\')'
                cursor.execute(statement)
                statement2 = 'insert into historial_tecnico(tecnico, equipo, fecha_inicio, fecha_fin, pais_equipo) values(\'' + row[0]+ '\',\'' + row[5]+ '\',\'' + row[6]+ '\',\'' + row[7]+ '\',\'' + row[4]+'\')'
                cursor.execute(statement2)
                connection.commit()
        elif option == 3:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into equipo(nombre, fecha_open, pais) values(\'' + row[0]+ '\',\'' + row[1]+ '\',\'' + row[2]+'\')'
                cursor.execute(statement)
                connection.commit()
        elif option == 4:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into jugador(nombre, fecha_nac, nacion, posicion) values(\'' + row[0]+ '\',\'' + row[1]+ '\',\'' + row[2]+ '\',\'' + row[3]+'\')'
                cursor.execute(statement)
                statement2 = 'insert into historial_jugador(jugador, equipo, fecha_ini, fecha_fin, pais_equipo) values(\'' + row[0]+ '\',\'' + row[5]+ '\',\'' + row[6]+ '\',\'' + row[7]+ '\',\'' + row[4]+'\')'
                cursor.execute(statement2)
                connection.commit()
        elif option == 5:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into competicion(nombre, tipo, pais) values(\'' + row[0]+ '\',\'' + row[2]+ '\',\'' + row[5]+'\')'
                cursor.execute(statement)
                statement2 = 'insert into historial_equipos(equipo, competicion, pais_equipo, anio, pais_campeon, campeon) values(\'' + row[7]+ '\',\'' + row[0]+ '\',\'' + row[6]+ '\',\'' + row[1]+ '\',\'' + row[3]+ '\',\'' + row[4]+'\')'
                cursor.execute(statement2)
                connection.commit()
        elif option == 6:
            for row in csv_f:
                connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
                cursor= connection.cursor()
                statement = 'insert into partido(fecha, asistencia, estadio, local, visita, estado, pais_local, pais_visita, competicion, anio) values(\'' + row[0]+ '\',\'' + row[4]+ '\',\'' + row[2]+ '\',\''+ row[6]+ '\',\''+ row[8]+ '\',\''+ row[3]+ '\',\''+ row[5]+ '\',\''+ row[7]+ '\',\''+ row[14]+ '\',\''+ row[15]+'\')'
                cursor.execute(statement)
                statement2 = 'insert into incidencia(incidencia, minuto, jugador, equipo, estadio, fecha, marcador) values(\'' + row[10]+ '\',\'' + row[11]+ '\',\'' + row[13]+ '\',\'' + row[12]+ '\',\'' + row[2]+ '\',\'' + row[0]+ '\',\''+ row[9]+'\')'
                cursor.execute(statement2)
                connection.commit()
        
        return render(request, 'carga.html', {'form': carga()})
    return render(request, 'carga.html', {'form': carga()})


def reporte1(request):
    form = rep1(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select \'Jugador\' , historial_jugador.jugador  from historial_jugador Where historial_jugador.EQUIPO =\''+ x + '\' And (to_date(historial_jugador.FECHA_FIN,\'DD/MM/YYYY\') >= sysdate -1 OR historial_jugador.FECHA_FIN =\' \' OR historial_jugador.FECHA_FIN IS NULL) UNION select \'Tecnico\' , historial_tecnico.tecnico  from historial_tecnico Where historial_tecnico.EQUIPO =\'' + x + '\' And (to_date(historial_tecnico.FECHA_FIN,\'DD/MM/YYYY\') >= sysdate -1 OR historial_tecnico.FECHA_FIN =\' \' OR historial_tecnico.FECHA_FIN IS NULL)'
        cursor.execute(statement)
        return render(request, 'reporte1.html',{'result': cursor.fetchall(), form:rep1()})
    return render(request, 'reporte1.html',{'form': rep1()})


def reporte2(request):
    form = rep2(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select \'Jugador\' ,NOMBRE , months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,\'DD/MM/YYYY\'))/12 as edad  from  jugador where months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,\'DD/MM/YYYY\'))/12  > '+ x+ 'UNION select \'Director\' ,tecnico.NOMBRE , months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,\'DD/MM/YYYY\'))/12  as edad  from  tecnico where months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,\'DD/MM/YYYY\'))/12 >' + x  
        cursor.execute(statement)
        return render(request, 'reporte2.html',{'result': cursor.fetchall(), form:rep2()})
    return render(request, 'reporte2.html',{'form': rep2()})



def reporte3(request):
    form = rep3(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select \'Jugador\' ,NOMBRE , months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,\'DD/MM/YYYY\'))/12  as edad  from  jugador where months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,\'DD/MM/YYYY\'))/12  < '+ x+ 'UNION select \'Director\' ,tecnico.NOMBRE , months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,\'DD/MM/YYYY\'))/12  as edad  from  tecnico where months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,\'DD/MM/YYYY\'))/12 <' + x  
        cursor.execute(statement)
        return render(request, 'reporte3.html',{'result': cursor.fetchall(), form:rep3()})
    return render(request, 'reporte3.html',{'form': rep3()})


def reporte4(request):
    form = rep4(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select historial_equipos.COMPETICION , historial_equipos.Anio, historial_equipos.EQUIPO  from  historial_equipos where historial_equipos.competicion = \''+x + '\''
        cursor.execute(statement)
        return render(request, 'reporte4.html',{'result': cursor.fetchall(), form:rep4()})
    return render(request, 'reporte4.html',{'form': rep4()})


def reporte5(request):
    form = rep5(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select pais, NOMBRE from  equipo where pais = \''+ x +   '\'' 
        cursor.execute(statement)
        return render(request, 'reporte5.html',{'result': cursor.fetchall(), form:rep5()})
    return render(request, 'reporte5.html',{'form': rep5()})


def reporte6(request):
    form = rep6(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select FECHA_OPEN, NOMBRE from  equipo where round(months_between(TRUNC(sysdate),to_date(FECHA_OPEN ,\'YYYY\'))/12 )  = ' + x 
        cursor.execute(statement)
        return render(request, 'reporte6.html',{'result': cursor.fetchall(), form:rep6()})
    return render(request, 'reporte6.html',{'form': rep6()})


def reporte7(request):
    form = rep7(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select pais, NOMBRE from  estadio where pais = \''+ x +  '\'' 
        cursor.execute(statement)
        return render(request, 'reporte7.html',{'result': cursor.fetchall(), form:rep7()})
    return render(request, 'reporte7.html',{'form': rep7()})


def reporte8(request):
    form = rep8(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  NOMBRE, capacidad from  estadio where capacidad <=  ' + x 
        cursor.execute(statement)
        return render(request, 'reporte8.html',{'result': cursor.fetchall(), form:rep8()})
    return render(request, 'reporte8.html',{'form': rep8()})


def reporte9(request):
    form = rep9(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.Local = \'' + x + '\' OR partido.visita =\'' + x + '\')  And to_date(FECHA,\'DD/MM/YYYY\') <= sysdate -1  ;' 
        cursor.execute(statement)
        return render(request, 'reporte9.html',{'result': cursor.fetchall(), form:rep9()})
    return render(request, 'reporte9.html',{'form': rep9()})


def reporte10(request):
    form = rep10(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select \'Jugador\', JUGADOR, EQUIPO from  historial_jugador where JUGADOR = \'' + x + '\' UNION select \'Tecnico\', historial_tecnico.TECNICO, historial_tecnico.EQUIPO from  historial_tecnico where historial_tecnico.TECNICO = \''+ x + '\'' 
        cursor.execute(statement)
        return render(request, 'reporte10.html',{'result': cursor.fetchall(), form:rep10()})
    return render(request, 'reporte10.html',{'form': rep10()})


def reporte11(request):
    form = rep11(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select incidencia.fecha, incidencia.estadio, partido.local, partido.visita, max(SUBSTR(incidencia.MARCADOR,1, 1) + SUBSTR(incidencia.MARCADOR,3, 1)) as diferencia from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia = \'Gol\' and SUBSTR(incidencia.MARCADOR,1, 1) + SUBSTR(incidencia.MARCADOR,3, 1) >= ' + x + ' Group by incidencia.fecha, incidencia.estadio, partido.local, partido.visita ' 
        cursor.execute(statement)
        return render(request, 'reporte11.html',{'result': cursor.fetchall(), form:rep11()})
    return render(request, 'reporte11.html',{'form': rep11()})


def reporte12(request):
    form = rep12(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        y = datos.get("y")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select * from (  select partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, count(*) as Cantidad from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia =\'' + x + '\' and partido.competicion = \''+ y + '\' Group by partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA Order by cantidad DESC) where rownum <= 5 ' 
        cursor.execute(statement)
        return render(request, 'reporte12.html',{'result': cursor.fetchall(), form:rep12()})
    return render(request, 'reporte12.html',{'form': rep12()})


def reporte13(request):
    form = rep13(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        y = datos.get("y")
        z = datos.get("z")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select * from (  select partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, count(*) as Cantidad,extract(year from to_date(incidencia.fecha ,\'DD/MM/YYYY\')) as Anio from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia =\''+ x + '\' and partido.competicion = \'' + y + '\' and extract(year from to_date(incidencia.fecha ,\'DD/MM/YYYY\')) = ' + z + ' Group by partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, extract(year from to_date(incidencia.fecha ,\'DD/MM/YYYY\')) Order by cantidad DESC) where rownum <= 5 ' 
        cursor.execute(statement)
        return render(request, 'reporte13.html',{'result': cursor.fetchall(), form:rep13()})
    return render(request, 'reporte13.html',{'form': rep13()})


def reporte14(request):
    form = rep14(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        y = datos.get("y")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select * from ( select  COMPETICION, campeon, count(distinct anio) as total from  historial_equipos group by competicion, campeon) where competicion = \'' + x + '\' and campeon = \'' + y + '\'' 
        cursor.execute(statement)
        return render(request, 'reporte14.html',{'result': cursor.fetchall(), form:rep14()})
    return render(request, 'reporte14.html',{'form': rep14()})


def reporte15(request):
    form = rep15(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = ' select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where extract(year from to_date(partido.fecha ,\'DD/MM/YYYY\')) =' + x 
        cursor.execute(statement)
        return render(request, 'reporte15.html',{'result': cursor.fetchall(), form:rep15()})
    return render(request, 'reporte15.html',{'form': rep15()})


def reporte16(request):
    form = rep16(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        y = datos.get("y")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.LOCAL = \''+ x + '\'  And VISITA = \'' + y + '\' OR partido.LOCAL = \''+ y + '\'  And VISITA = \''+ x + '\') And to_date(FECHA,\'DD/MM/YYYY\') >= sysdate -1  ' 
        cursor.execute(statement)
        return render(request, 'reporte16.html',{'result': cursor.fetchall(), form:rep16()})
    return render(request, 'reporte16.html',{'form': rep16()})


def reporte17(request):
    form = rep17(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.LOCAL = \''+ x +'\'  OR VISITA = \''+ x + '\' )And to_date(FECHA,\'DD/MM/YYYY\') >= sysdate -1  ' 
        cursor.execute(statement)
        return render(request, 'reporte17.html',{'result': cursor.fetchall(), form:rep17()})
    return render(request, 'reporte17.html',{'form': rep17()})


def areporte1(request):
    form = arep1(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select USUARIO.usuario, CORREO, SUSCRITO from usuario where  tipo=3 and SUSCRITO =\'' + x +'\'' 
        cursor.execute(statement)
        return render(request, 'areporte1.html',{'result': cursor.fetchall(), form:arep1()})
    return render(request, 'areporte1.html',{'form': arep1()})


def areporte2(request):
    form = arep2(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        if x == '1':
            connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
            cursor= connection.cursor()
            statement = 'select USUARIO.usuario, CORREO, SUSCRITO from usuario, membresia where usuario.USUARIO= membresia.USUARIO And sysdate > membresia.FECHA_GENERADO and sysdate < membresia.FECHA_FIN'
            cursor.execute(statement)
        elif x=='0':
            connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
            cursor= connection.cursor()
            statement = 'select USUARIO.usuario, CORREO, SUSCRITO from usuario, membresia where usuario.USUARIO= membresia.USUARIO And (sysdate < membresia.FECHA_GENERADO or sysdate > membresia.FECHA_FIN)' 
            cursor.execute(statement)
        else:
            connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
            cursor= connection.cursor()
            statement = 'select USUARIO.usuario, CORREO, SUSCRITO from usuario, membresia where usuario.USUARIO= membresia.USUARIO And (sysdate < membresia.FECHA_GENERADO or sysdate > membresia.FECHA_FIN)'   
            cursor.execute(statement)
        return render(request, 'areporte2.html',{'result': cursor.fetchall(), form:arep2()})
    return render(request, 'areporte2.html',{'form': arep2()})



def areporte3(request):
    form = arep3(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select USUARIO.usuario, usuario.CORREO, count(*) as Subscripciones from usuario, membresia where usuario.USUARIO= membresia.USUARIO Group by usuario.usuario, usuario.correo order by Subscripciones DESC'
        cursor.execute(statement)
        return render(request, 'areporte3.html',{'result': cursor.fetchall(), form:arep3()})
    return render(request, 'areporte3.html',{'form': arep3()})


def areporte4(request):
    form = arep4(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select USUARIO.usuario, usuario.CORREO, sum(membresia.PRECIO) as Total  from usuario, membresia where usuario.USUARIO= membresia.USUARIO Group by usuario.usuario, usuario.correo order by Total DESC'
        cursor.execute(statement)
        return render(request, 'areporte4.html',{'result': cursor.fetchall(), form:arep4()})
    return render(request, 'areporte4.html',{'form': arep4()})


def areporte5(request):
    form = arep5(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select USUARIO.usuario, CORREO, SUSCRITO from usuario where (tipo = 4 OR tipo=3) and PAIS =\''+ x +   '\'' 
        cursor.execute(statement)
        return render(request, 'areporte5.html',{'result': cursor.fetchall(), form:arep5()})
    return render(request, 'areporte5.html',{'form': arep5()})


def areporte6(request):
    form = arep6(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'sselect USUARIO.usuario, CORREO, SUSCRITO from usuario where (tipo = 4 OR tipo=3) and GENERO =\''+ x +  '\'' 
        cursor.execute(statement)
        return render(request, 'areporte6.html',{'result': cursor.fetchall(), form:arep6()})
    return render(request, 'areporte6.html',{'form': arep6()})


def areporte7(request):
    form = arep7(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select USUARIO.usuario, CORREO, SUSCRITO  from usuario where (tipo = 4 OR tipo=3) and months_between(TRUNC(sysdate),to_date(FECHA_NACIMIENTO ,\'DD/MM/YYYY\'))/12 <='+ x 
        cursor.execute(statement)
        return render(request, 'areporte7.html',{'result': cursor.fetchall(), form:arep7()})
    return render(request, 'areporte7.html',{'form': arep7()})


def areporte8(request):
    form = arep8(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  NOMBRE, capacidad from  estadio where capacidad <=  ' + x 
        cursor.execute(statement)
        return render(request, 'areporte8.html',{'result': cursor.fetchall(), form:arep8()})
    return render(request, 'areporte8.html',{'form': arep8()})


def areporte9(request):
    form = arep9(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.Local = \'' + x + '\' OR partido.visita =\'' + x + '\')  And to_date(FECHA,\'DD/MM/YYYY\') <= sysdate -1  ;' 
        cursor.execute(statement)
        return render(request, 'areporte9.html',{'result': cursor.fetchall(), form:arep9()})
    return render(request, 'areporte9.html',{'form': arep9()})


def areporte10(request):
    form = arep10(request.POST)
    variables={
        "form":form,
    }
    if form.is_valid():  
        datos = form.cleaned_data      
        x = datos.get("x")
        connection = cx_Oracle.connect("ARCHIVOS/stark@localhost/XE")
        cursor= connection.cursor()
        statement = 'select \'Jugador\', JUGADOR, EQUIPO from  historial_jugador where JUGADOR = \'' + x + '\' UNION select \'Tecnico\', historial_tecnico.TECNICO, historial_tecnico.EQUIPO from  historial_tecnico where historial_tecnico.TECNICO = \''+ x + '\'' 
        cursor.execute(statement)
        return render(request, 'areporte10.html',{'result': cursor.fetchall(), form:arep10()})
    return render(request, 'areporte10.html',{'form': arep10()})

