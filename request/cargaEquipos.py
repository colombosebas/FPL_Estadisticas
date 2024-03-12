import requests
from entidades.equipo import Equipo

def obtener_equipos_desde_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        data = response.json()
        equipos = []
        standigs = data.get("standings", {}).get("results", [])
        for equipo_data in standigs:
            codigo = equipo_data.get("entry")
            nombre = equipo_data.get("entry_name")
            manager = equipo_data.get("player_name")
            equipo = Equipo(codigo, nombre, manager)
            equipos.append(equipo)

        return equipos
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None

if __name__ == "__main__":
    # URL de la API
    url_api = "https://fantasy.premierleague.com/api/leagues-classic/294608/standings?page_standings=1"

    # Obtener equipos desde la API
    equipos = obtener_equipos_desde_api(url_api)

    # Imprimir los equipos
    if equipos:
        print("Equipos obtenidos correctamente:")
        for equipo in equipos:
            print(equipo)
    else:
        print("No se pudieron obtener los equipos.")