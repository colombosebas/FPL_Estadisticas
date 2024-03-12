import requests
from entidades.jugador import Player


def obtener_jugadores_desde_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        data = response.json()
        jugadores = []
        # Diccionario para mapear element_type a posiciones
        tipo_posicion = {
            1: "Golero",
            2: "Defensa",
            3: "Mediocampista",
            4: "Delantero"
        }

        for jugador_data in data['elements']:
            codigo = jugador_data['code']
            nombre = jugador_data['web_name']
            id = jugador_data['id']
            element_type = jugador_data['element_type']
            posicion = tipo_posicion.get(element_type, "Desconocido")
            club = jugador_data['team_code']
            jugador = Player(codigo, nombre, id, posicion, club)
            jugadores.append(jugador)

        return jugadores
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None

if __name__ == "__main__":
    # URL de la API
    url_api = "https://fantasy.premierleague.com/api/bootstrap-static/"

    # Obtener jugadores desde la API
    jugadores = obtener_jugadores_desde_api(url_api)

    # Imprimir los jugadores
    if jugadores:
        print("Jugadores obtenidos correctamente:")
        for jugador in jugadores:
            print(jugador)
    else:
        print("No se pudieron obtener los jugadores.")