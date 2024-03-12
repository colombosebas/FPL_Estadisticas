from typing import List

from entidades.equipo_estadisticas import EquipoEstadistica
from entidades.jugador import Player
from request.cargaClubes import obtener_clubes_desde_api
from request.cargaEquipos import obtener_equipos_desde_api
from request.cargaJugadores import obtener_jugadores_desde_api
from request.cargarEquipoEstadisticas import obtener_equiposEstadisticas_desde_api
from request.cargarEquipoEstadisticasJugador import obtener_equiposEstadisticasJugador_desde_api


def cargaDatosBases():
    url_api = "https://fantasy.premierleague.com/api/bootstrap-static/"
    url_api2 = "https://fantasy.premierleague.com/api/leagues-classic/294608/standings?page_standings=1"
    jugadores = obtener_jugadores_desde_api(url_api)
    clubes = obtener_clubes_desde_api(url_api)
    equipos = obtener_equipos_desde_api(url_api2)
    return jugadores, clubes, equipos

def cargarEstadisticas(equipos):
    estadisticas = []
    for equipo in equipos:
        url =  f"https://fantasy.premierleague.com/api/entry/{equipo.codigo}/history"
        EquipoEst = obtener_equiposEstadisticas_desde_api(url, equipo.nombre, equipo.manager, equipo.codigo)
        estadisticas.append(EquipoEst)
    return estadisticas

def estadisticasGenerales(estadisticas):
    max_point_manager = None
    max_point_fecha = None
    max_point_pts = 0
    min_point_manager = None
    min_point_pts = 100
    min_point_fecha = None

    for equipoEst in estadisticas:

        # Máxima Semana
        if equipoEst.max_point_pts > max_point_pts:
            max_point_pts = equipoEst.max_point_pts
            max_point_manager = equipoEst.manager
            max_point_fecha = equipoEst.max_point_fecha

        # Mínima Semana
        if equipoEst.min_point_pts < min_point_pts:
            min_point_pts = equipoEst.min_point_pts
            min_point_manager = equipoEst.manager
            min_point_fecha = equipoEst.min_point_fecha

    print(f'{max_point_manager} hizo la mayor cantidad de puntos en una fecha: {max_point_pts}. Fue en la fecha {max_point_fecha}')
    print(f'{min_point_manager} hizo la menor cantidad de puntos en una fecha: {min_point_pts}. Fue en la fecha {min_point_fecha}')
    #Mas cost transfer
    print('---------Costos de puntos en trasnfers---------')
    manager_cost_pairs = [(equipoEst.manager, equipoEst.cost_transfer) for equipoEst in estadisticas]
    manager_cost_pairs_sorted = sorted(manager_cost_pairs, key=lambda x: x[1], reverse=True)
    for manager, cost_transfer in manager_cost_pairs_sorted:
        print(f"{manager} - {cost_transfer}")
    print('')
    print('---------Puntos dejados en el banco---------')
    manager_points_bench = [(equipoEst.manager, equipoEst.points_bench) for equipoEst in estadisticas]
    manager_points_bench_sorted = sorted(manager_points_bench, key=lambda x: x[1], reverse=True)
    for manager, points_bench in manager_points_bench_sorted:
        print(f"{manager} - {points_bench}")
    print('')

def estadisticasGenerales2(estadisticas):
    print('---------Puntos de capitán---------')
    manager_points_captain = [(equipoEst.manager, equipoEst.points_captain) for equipoEst in estadisticas]
    manager_points_captain_sorted = sorted(manager_points_captain, key=lambda x: x[1], reverse=True)
    for manager, points_captain in manager_points_captain_sorted:
        print(f"{manager} - {points_captain}")
    print('')
    print('---------Cantidad de jugadores utilizazdos---------')
    cant_used_player = [(equipoEst.manager, equipoEst.cant_used_player) for equipoEst in estadisticas]
    cant_used_player_sorted = sorted(cant_used_player, key=lambda x: x[1], reverse=True)
    for manager, cant_used_player in cant_used_player_sorted:
        print(f"{manager} - {cant_used_player}")
    print('')

def semanasGanadas(estadisticas):
    nueva_coleccion = []
    # Recorrer las semanas de la primera equipo_estadisticas
    for semana in estadisticas[0].weeks:
        # Obtener el número de semana
        numero_semana = semana["Week"]
        # Inicializar variables para almacenar el máximo total de puntos y el manager asociado
        max_total_points = 0
        manager_max_points = None
        # Recorrer cada objeto equipoEst en la colección
        for equipo in estadisticas:
            # Recorrer cada semana en la lista Weeks del objeto equipoEst actual
            for semana_equipo in equipo.weeks:
                # Verificar si esta semana coincide con la semana actual en el bucle externo
                if semana_equipo["Week"] == numero_semana:
                    # Obtener el total de puntos para esta semana
                    total_points = semana_equipo["TotalPoint"]
                    # Verificar si este total de puntos es mayor al máximo encontrado hasta ahora
                    if total_points > max_total_points:
                        max_total_points = total_points
                        manager_max_points = equipo.manager
                    elif total_points == max_total_points:
                        manager_max_points = f'{manager_max_points}, {equipo.manager}'
                    break  # Salir del bucle interno, ya hemos encontrado la semana actual en este equipo
        # Agregar la semana, el manager y el total de puntos a la nueva colección
        nueva_coleccion.append({"Week": numero_semana, "Manager": manager_max_points, "Points": max_total_points})

    #Actualizo winner week
    for semana in nueva_coleccion:
        managers_ganadores = semana["Manager"].split(", ")
        for manager_ganador in managers_ganadores:
            for equipo in estadisticas:
                if equipo.manager == manager_ganador:
                    equipo.winner_week += 1
                    break

    print('---------Ganadores de cada semana---------')
    for item in nueva_coleccion:
        print(item)
    print('')

def semanasUltimo(estadisticas):
    nueva_coleccion = []
    # Recorrer las semanas de la primera equipo_estadisticas
    for semana in estadisticas[0].weeks:
        # Obtener el número de semana
        numero_semana = semana["Week"]
        # Inicializar variables para almacenar el máximo total de puntos y el manager asociado
        min_total_points = 1000
        manager_min_points = None
        # Recorrer cada objeto equipoEst en la colección
        for equipo in estadisticas:
            # Recorrer cada semana en la lista Weeks del objeto equipoEst actual
            for semana_equipo in equipo.weeks:
                # Verificar si esta semana coincide con la semana actual en el bucle externo
                if semana_equipo["Week"] == numero_semana:
                    # Obtener el total de puntos para esta semana
                    total_points = semana_equipo["TotalPoint"]
                    # Verificar si este total de puntos es mayor al máximo encontrado hasta ahora
                    if total_points < min_total_points:
                        min_total_points = total_points
                        manager_min_points = equipo.manager
                    elif total_points == min_total_points:
                        manager_min_points = f'{manager_min_points}, {equipo.manager}'
                    break  # Salir del bucle interno, ya hemos encontrado la semana actual en este equipo
        # Agregar la semana, el manager y el total de puntos a la nueva colección
        nueva_coleccion.append({"Week": numero_semana, "Manager": manager_min_points, "Points": min_total_points})

    #Actualizo winner week
    for semana in nueva_coleccion:
        managers_perdedores = semana["Manager"].split(", ")
        for manager_perdedor in managers_perdedores:
            for equipo in estadisticas:
                if equipo.manager == manager_perdedor:
                    equipo.lost_week += 1
                    break

    print('---------Fracasados de cada semana---------')
    for item in nueva_coleccion:
        print(item)
    print('')

def estadisticasGenerales3(estadisticas):
    print('---------Semanas Ganadas---------')
    manager_winner_week = [(equipoEst.manager, equipoEst.winner_week) for equipoEst in estadisticas]
    manager_winner_week_sorted = sorted(manager_winner_week, key=lambda x: x[1], reverse=True)
    for manager, winner_week in manager_winner_week_sorted:
        print(f"{manager} - {winner_week}")
    print('')
    print('---------Semanas Último---------')
    manager_lost_week = [(equipoEst.manager, equipoEst.lost_week) for equipoEst in estadisticas]
    manager_lost_week_sorted = sorted(manager_lost_week, key=lambda x: x[1], reverse=True)
    for manager, lost_week in manager_lost_week_sorted:
        print(f"{manager} - {lost_week}")
    print('')

def estadisticasGeneralesJugadores(equiposEst: List[EquipoEstadistica], jugadores: List[Player]):
    for equipo in equiposEst:
        obtener_equiposEstadisticasJugador_desde_api(28,jugadores, equipo)
        #print(equipo)

jugadores, clubes, equipos = cargaDatosBases()
estadisticas = cargarEstadisticas(equipos)
estadisticasGenerales(estadisticas)
estadisticasGeneralesJugadores(estadisticas, jugadores)
estadisticasGenerales2(estadisticas)
semanasGanadas(estadisticas)
semanasUltimo(estadisticas)
estadisticasGenerales3(estadisticas)
for equipo in estadisticas:
    print(equipo)