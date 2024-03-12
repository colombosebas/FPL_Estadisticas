import requests
from entidades.club import Club

def obtener_clubes_desde_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        data = response.json()
        clubes = []

        for team_data in data['teams']:
            codigo = team_data['code']
            nombre = team_data['name']
            club = Club(codigo, nombre)
            clubes.append(club)

        return clubes
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None

if __name__ == "__main__":
    # URL de la API
    url_api = "https://fantasy.premierleague.com/api/bootstrap-static/"

    # Obtener clubes desde la API
    clubes = obtener_clubes_desde_api(url_api)

    # Imprimir los clubes
    if clubes:
        print("Clubes obtenidos correctamente:")
        for club in clubes:
            print(club)
    else:
        print("No se pudieron obtener los clubes.")