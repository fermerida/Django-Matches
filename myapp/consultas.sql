CLIENTE
inicial: select partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION, max(incidencia.Marcador) from partido, incidencia where partido.Estadio = incidencia.Estadio and partido.fecha = incidencia.fecha and partido.estado= 'Finalizado' Group by partido.Estadio, partido.FECHA, partido.LOCAL, partido.VISITA, partido.COMPETICION;
1)select 'Jugador' , historial_jugador.jugador  from historial_jugador Where historial_jugador.EQUIPO ='Barcelona' And (to_date(historial_jugador.FECHA_FIN,'DD/MM/YYYY') >= sysdate -1 OR historial_jugador.FECHA_FIN =' ' OR historial_jugador.FECHA_FIN IS NULL) UNION select 'Tecnico' , historial_tecnico.tecnico  from historial_tecnico Where historial_tecnico.EQUIPO ='Barcelona' And (to_date(historial_tecnico.FECHA_FIN,'DD/MM/YYYY') >= sysdate -1 OR historial_tecnico.FECHA_FIN =' ' OR historial_tecnico.FECHA_FIN IS NULL);  
2)select 'Jugador' ,NOMBRE , round(months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) as edad  from  jugador where months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,'DD/MM/YYYY'))/12 -1 > 27 UNION select 'Director' ,tecnico.NOMBRE , round(months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) as edad  from  tecnico where round(months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) > 27;  
3)select 'Jugador' ,NOMBRE , round(months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) as edad  from  jugador where months_between(TRUNC(sysdate),to_date(jugador.FECHA_NAC ,'DD/MM/YYYY'))/12 -1 < 27 UNION select 'Director' ,tecnico.NOMBRE , round(months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) as edad  from  tecnico where round(months_between(TRUNC(sysdate),to_date(tecnico.FECHA_NAC ,'DD/MM/YYYY'))/12 -1) < 27;  
4)select historial_equipos.COMPETICION , historial_equipos.Anio, historial_equipos.EQUIPO  from  historial_equipos where historial_equipos.competicion = 'LaLiga' and ANIO = 2017;  
5)select pais, NOMBRE from  equipo where pais = 'Espa�a'  
6)select FECHA_OPEN, NOMBRE from  equipo where round(months_between(TRUNC(sysdate),to_date(FECHA_OPEN ,'YYYY'))/12 )  = 118;  
7)select pais, NOMBRE from  estadio where pais = 'Espa�a';  
8)select  NOMBRE, capacidad from  estadio where capacidad <= 10000000;  
9)select  FECHA, ESTADIO, partido.LOCAL, VISITA from  partido where partido.Local = 'Barcelona' OR partido.visita ='Barcelona' ;  
10)select  JUGADOR, EQUIPO from  historial_jugador where JUGADOR = 'Ousmane Dembele' UNION select  historial_tecnico.TECNICO, historial_tecnico.EQUIPO from  historial_tecnico where historial_tecnico.TECNICO = 'Ousmane Dembele';   
11)select incidencia.fecha, incidencia.estadio, partido.local, partido.visita, max(SUBSTR(incidencia.MARCADOR,1, 1) + SUBSTR(incidencia.MARCADOR,3, 1)) as diferencia from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia = 'Gol' and SUBSTR(incidencia.MARCADOR,1, 1) + SUBSTR(incidencia.MARCADOR,3, 1) > 3 Group by incidencia.fecha, incidencia.estadio, partido.local, partido.visita ;  
12)select * from (  select partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, count(*) as Cantidad from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia ='Gol' and partido.competicion = 'LaLiga' Group by partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA Order by cantidad DESC) where rownum <= 5;  
13)select * from (  select partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, count(*) as Cantidad,extract(year from to_date(incidencia.fecha ,'DD/MM/YYYY')) as Anio from  incidencia, partido where incidencia.fecha = partido.fecha and incidencia.estadio = partido.estadio and incidencia.incidencia ='Gol' and partido.competicion = 'LaLiga' and extract(year from to_date(incidencia.fecha ,'DD/MM/YYYY')) = '2018' Group by partido.COMPETICION,incidencia.jugador, incidencia.INCIDENCIA, extract(year from to_date(incidencia.fecha ,'DD/MM/YYYY')) Order by cantidad DESC) where rownum <= 5;   
14)select * from ( select  COMPETICION, campeon, count(distinct anio) as total from  historial_equipos group by competicion, campeon) where competicion = 'LaLiga' and campeon = 'Real Madrid';  
15)select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where extract(year from to_date(partido.fecha ,'DD/MM/YYYY')) = 2019;  
16)select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.LOCAL = 'Chelsea'  And VISITA = 'Arsenal' OR partido.LOCAL = 'Arsenal'  And VISITA = 'Chelsea') And to_date(FECHA,'DD/MM/YYYY') >= sysdate -1  
17)select  ESTADIO, FECHA, partido.LOCAL, VISITA from  partido where (partido.LOCAL = 'Chelsea'  OR VISITA = 'Chelsea' )And to_date(FECHA,'DD/MM/YYYY') >= sysdate -1  



ADMIN
1) select USUARIO.usuario, CORREO, SUSCRITO from usuario where (tipo = 4 OR tipo=3) and SUSCRITO = 'Chelsea' 
2) select USUARIO.usuario, CORREO, SUSCRITO from usuario, membresia where usuario.USUARIO= membresia.USUARIO And (sysdate < membresia.FECHA_GENERADO or sysdate > membresia.FECHA_FIN);
select USUARIO.usuario, CORREO, SUSCRITO from usuario, membresia where usuario.USUARIO= membresia.USUARIO And sysdate > membresia.FECHA_GENERADO and sysdate < membresia.FECHA_FIN;
3)select USUARIO.usuario, usuario.CORREO, count(*) as Subscripciones from usuario, membresia where usuario.USUARIO= membresia.USUARIO Group by usuario.usuario, usuario.correo order by Subscripciones DESC;
4)select USUARIO.usuario, usuario.CORREO, sum(membresia.PRECIO) as Total  from usuario, membresia where usuario.USUARIO= membresia.USUARIO Group by usuario.usuario, usuario.correo order by Total DESC;
5)select USUARIO.usuario, CORREO, SUSCRITO from usuario where (tipo = 4 OR tipo=3) and PAIS = 'Guam' 
6)select USUARIO.usuario, CORREO, SUSCRITO from usuario where (tipo = 4 OR tipo=3) and GENERO = 'M'
7)select USUARIO.usuario, CORREO, SUSCRITO  from usuario where (tipo = 4 OR tipo=3) and months_between(TRUNC(sysdate),to_date(FECHA_NACIMIENTO ,'DD/MM/YYYY'))/12 <= 20
8)



insert into membresia (usuario, fecha_generado, precio) values ('prueba', sysdate, 15);