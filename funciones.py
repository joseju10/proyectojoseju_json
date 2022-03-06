import json
from operator import eq
with open("partidos_resultados.json") as fichero:
    datos_json=json.load(fichero)

def listar_informacion(jornada):
        pcont=0
        equipos=[]
        while pcont!=10:
                if 2 <= datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]:
                        equipos.append(datos_json["rounds"][jornada]["matches"][pcont]["team1"])
                if 2 <= datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]:
                        equipos.append(datos_json["rounds"][jornada]["matches"][pcont]["team2"])
                pcont=pcont+1
        print(equipos)

def contar_informacion(equipo):
        vcont=0
        jornadas=0
        while jornadas!=38:
                pcont=0
                while pcont!=10:
                        if equipo==(datos_json["rounds"][jornadas]["matches"][pcont]["team1"]) and 3 <= datos_json["rounds"][jornadas]["matches"][pcont]["score"]["ft"][0]:
                                vcont=vcont+1
                        if equipo==(datos_json["rounds"][jornadas]["matches"][pcont]["team2"]) and 3 <= datos_json["rounds"][jornadas]["matches"][pcont]["score"]["ft"][1]:
                                vcont=vcont+1
                        pcont=pcont+1
                jornadas=jornadas+1
        print("El equipo",equipo,"ha marcado mas de 3 goles en",vcont,"partidos")

def buscar_informacion(equipo,jornada):
        pcont=0
        while pcont!=10:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team1"]):
                        goles=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]
                        rival=datos_json["rounds"][jornada]["matches"][pcont]["team2"]
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team2"]):
                        goles=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]
                        rival=datos_json["rounds"][jornada]["matches"][pcont]["team1"]
                pcont=pcont+1
        print("El equipo",equipo,"le ha marcado",goles,"a",rival)

def informacion_relacionada(equipo,jornada):
        pcont=0
        while pcont!=10:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team1"]):
                        fecha_partido=(datos_json["rounds"][jornada]["matches"][pcont]["date"])
                        rival=(datos_json["rounds"][jornada]["matches"][pcont]["team2"])
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team2"]):
                        fecha_partido=(datos_json["rounds"][jornada]["matches"][pcont]["date"])
                        rival=(datos_json["rounds"][jornada]["matches"][pcont]["team1"])
                pcont=pcont+1
        print("El equipo",equipo,"juega contra",rival,"el día",fecha_partido)

def mostrar_victorias(equipo):
        jcont=0
        victorias=0
        empates=0
        derrotas=0
        while jcont!=38:
                pcont=0
                while pcont!=10:
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team1"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]<datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]:
                                victorias=victorias+1
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team2"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]<datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]:
                                victorias=victorias+1
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team1"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]==datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]:
                                empates=empates+1
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team2"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]==datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]:
                                empates=empates+1
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team1"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]<datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]:
                                derrotas=derrotas+1
                        if equipo==(datos_json["rounds"][jcont]["matches"][pcont]["team2"]) and datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][1]<datos_json["rounds"][jcont]["matches"][pcont]["score"]["ft"][0]:
                                derrotas=derrotas+1
                        pcont=pcont+1
                jcont=jcont+1
        print("El equipo",equipo,"ha ganado:",victorias,"partidos, ha empatado:",empates,"partidos y ha perdido:",derrotas,"partidos.")