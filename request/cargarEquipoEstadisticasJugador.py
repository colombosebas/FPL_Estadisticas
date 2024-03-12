import requests
from entidades.equipo_estadisticas import EquipoEstadistica

def obtener_equiposEstadisticasJugador_desde_api(x, jugadores, equipo:EquipoEstadistica):
    for i in range(1, x + 1):#recorro cada fecha
        try:
            url = f'https://fantasy.premierleague.com/api/event/{i}/live/'#Los datos de la fecha
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
            dataFecha = response.json()
            jugadorFecha = dataFecha["elements"]
            url = f'https://fantasy.premierleague.com/api/entry/{equipo.codigo}/event/{i}/picks/'#Los datos del equipo en la fecha
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
            dataEquipoFecha = response.json()
            picks = dataEquipoFecha["picks"]
            for pick in picks:#recorro cada jugador de la fecha
                name = ''
                points = 0
                element_id = pick["element"]
                multiplier = pick["multiplier"]
                for jugador in jugadores:
                    if element_id == jugador.id:
                        name = jugador.nombre
                        break
                if multiplier == 0:
                    points = 0
                else:
                    for item in jugadorFecha:
                        if element_id == item["id"]:
                            points = item['stats']['total_points']
                            break
                existeJugador = False
                if multiplier > 1:
                    capitan = 1
                    equipo.points_captain = int(equipo.points_captain) + (points * multiplier)
                else:
                    capitan = 0
                for jugador in equipo.players:
                    if jugador['Name'] == name:
                        existeJugador = True
                        jugador['Matchs'] = int(jugador['Matchs']) + 1
                        jugador['Points'] = int(jugador['Points']) + (points * multiplier)
                        if multiplier > 1:
                            jugador['Capitan'] = int(jugador['Capitan']) + 1
                        break
                if not existeJugador:
                    new_player = {
                        'Name': name,
                        'Matchs': 1,
                        'Points': points,
                        'Capitan': capitan
                    }
                    equipo.players.append(new_player)
        except requests.exceptions.RequestException as e:
            print("Error al realizar la solicitud:", e)
            return None
    equipo.players = sorted(equipo.players, key=lambda x: x["Points"], reverse=True)
    equipo.cant_used_player = len(equipo.players)
    return equipo