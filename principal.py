#Abrimos el arvhivo partidos_resultados_JSON.
import json
from operator import eq
with open("partidos_resultados.json") as fichero:
    datos_json=json.load(fichero)
from funciones import *
opciones='''
1.Listar equipos que hayan marcado mas de los goles que especifiques o mas en una jornada.
2.Contar partidos de un equipo en los que haya marcado una cantidad de goles especificada.
3.Buscar la cantidad de goles que le ha marcado a un equipo en una jornada indicada.
4.Informacion Relacionada preguntando el equipo y una jornada, y mostramos el marcador, rival y si ha ganado,empatado o perdido.
5.Pide el nombre de un equipo y muestra el numero de victorias, empates y derrotas.
6.Salir'''
#Listar el nombre de los equipos que han marcado dos goles o más en la jornada que usted especifique.
print(opciones)
opcion=int(input("Opción:"))
while opcion!=6:
    if opcion==1:
        jornada=int(input("INTRODUZCA LA JORNADA QUE VAYA A BUSCAR [0-37]:"))
        goles=int(input("INTRODUZCA LA CANTIDAD DE GOLES:"))
        listar_informacion(jornada,goles)
    if opcion==2:
        equipo=input("INTRODUZCA EL NOMBRE DEL EQUIPO:")
        goles=int(input("INTRODUZCA LA CANTIDAD DE GOLES:"))
        contar_informacion(equipo,goles)
    if opcion==3:
        equipo=input("INTRODUZCA EL NOMBRE DEL EQUIPO:")
        jornada=int(input("INTRODUZCA LA JORNADA 0-37:"))
        buscar_informacion(equipo,jornada)
    if opcion==4:
        equipo=input("INTRODUZCA EL NOMBRE DEL EQUIPO:")
        jornada=int(input("INTRODUZCA LA JORNADA 0-37:"))
        informacion_relacionada(equipo,jornada)
    if opcion==5:
        equipo=input("INTRODUZCA EL NOMBRE DEL EQUIPO:")
        mostrar_victorias(equipo)
    print(opciones)
    opcion=int(input("Opción:"))