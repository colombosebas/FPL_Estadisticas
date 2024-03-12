import requests
from entidades.equipo_estadisticas import EquipoEstadistica

def obtener_equiposEstadisticas_desde_api(url, name, manager, codigo):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        data = response.json()
        current = data["current"]
        max_point_pts = max(current, key=lambda x: x["points"])["points"]
        max_point_fecha = max(current, key=lambda x: x["points"])["event"]
        min_point_pts = min(current, key=lambda x: x["points"])["points"]
        min_point_fecha = min(current, key=lambda x: x["points"])["event"]
        points_bench = sum(item["points_on_bench"] for item in current)
        cost_transfer = sum(item["event_transfers_cost"] for item in current)

        weeks = [
            {"Week": item["event"], "Points": item["points"], "Bench": item["points_on_bench"], "Cost": item["event_transfers_cost"]}
            for item in current]
        players = []
        print(weeks)
        for week in weeks:
            week['TotalPoint'] = int(week['Points']) - int(week['Cost'])
        equipoEst = EquipoEstadistica(
            equipo=name,
            manager=manager,
            codigo=codigo,
            max_point_fecha=max_point_fecha,
            max_point_pts=max_point_pts,
            min_point_fecha=min_point_fecha,
            min_point_pts=min_point_pts,
            points_bench=points_bench,
            points_captain=None,  # You need to figure out this value
            winner_month=None,  # You need to figure out this value
            max_position_month=None,  # You need to figure out this value
            min_position_month=None,  # You need to figure out this value
            cost_transfer=cost_transfer,
            winner_week=None,  # You need to figure out this value
            lost_week=None,  # You need to figure out this value
            cant_used_player = None,
            weeks=weeks,
            players=players  # You need to figure out this value
        )
        return equipoEst
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None

if __name__ == "__main__":
    # URL de la API
    url_api = "https://fantasy.premierleague.com/api/entry/309285/history"

    # Obtener equipos desde la API
    equipoEst = obtener_equiposEstadisticas_desde_api(url_api, "LukakuVolveAEverton","Sebastián")
    # Imprimir las estadísticas
    print(equipoEst)