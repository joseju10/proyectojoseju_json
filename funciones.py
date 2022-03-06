import json
from operator import eq
with open("partidos_resultados.json") as fichero:
    datos_json=json.load(fichero)

def listar_informacion(jornada,goles):
        pcont=0
        equipos=[]
        while pcont!=10:
                if goles <= datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]:
                        equipos.append(datos_json["rounds"][jornada]["matches"][pcont]["team1"])
                if goles <= datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]:
                        equipos.append(datos_json["rounds"][jornada]["matches"][pcont]["team2"])
                pcont=pcont+1
        print(equipos)

def contar_informacion(equipo,goles):
        vcont=0
        jornadas=0
        while jornadas!=38:
                pcont=0
                while pcont!=10:
                        if equipo==(datos_json["rounds"][jornadas]["matches"][pcont]["team1"]) and goles <= datos_json["rounds"][jornadas]["matches"][pcont]["score"]["ft"][0]:
                                vcont=vcont+1
                        if equipo==(datos_json["rounds"][jornadas]["matches"][pcont]["team2"]) and goles <= datos_json["rounds"][jornadas]["matches"][pcont]["score"]["ft"][1]:
                                vcont=vcont+1
                        pcont=pcont+1
                jornadas=jornadas+1
        print("El equipo",equipo,"ha marcado mas de",goles,"goles en",vcont,"partidos")

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
                #victoria
                #si el equipo indicado es el equipo1 y le ganó al equipo2:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team1"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]<datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team2"]
                        print("El equipo,",equipo,"se llevo la victoria ante el equipo",rival,"con el marcador de",marcador)
                #si el equipo indicado es el equipo2 y le ganó al equipo1:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team2"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]<datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team1"]
                        print("El equipo,",equipo,"se llevo la victoria ante el equipo",rival,"con el marcador de",marcador)
                #empate
                #si el equipo indicado es el equipo1 y empató con el equipo 2:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team1"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]==datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team2"]
                        print("El equipo,",equipo,"empató ante el equipo",rival,"con el marcador de",marcador)
                #si el equipo indicado es el equipo2 y empató con equipo1:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team2"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]==datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team1"]
                        print("El equipo,",equipo,"empató ante el equipo",rival,"con el marcador de",marcador)
                #derrota
                #si el equipo indicado es el equipo1 y perdió con el equipo2:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team1"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]<datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team2"]
                        print("El equipo,",equipo,"perdió ante el equipo",rival,"con el marcador de",marcador)
                #si el equipo indicado es el equipo2 y perdió con el equipo1:
                if equipo==(datos_json["rounds"][jornada]["matches"][pcont]["team2"]) and datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][1]<datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"][0]:
                        marcador=datos_json["rounds"][jornada]["matches"][pcont]["score"]["ft"]
                        rival=rival=datos_json["rounds"][jornada]["matches"][pcont]["team1"]
                        print("El equipo,",equipo,"perdió ante el equipo",rival,"con el marcador de",marcador)
                pcont=pcont+1

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