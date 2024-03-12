class EquipoEstadistica:
    def __init__(self, equipo, manager, codigo, max_point_fecha, max_point_pts, min_point_fecha, min_point_pts,
                 points_bench, points_captain, winner_month, max_position_month, min_position_month,
                 cost_transfer, winner_week, lost_week, cant_used_player, weeks, players):
        self.equipo = equipo
        self.manager = manager
        self.codigo = codigo
        self.max_point_fecha = max_point_fecha or 0
        self.max_point_pts = max_point_pts or 0
        self.min_point_fecha = min_point_fecha or 0
        self.min_point_pts = min_point_pts or 0
        self.points_bench = points_bench or 0
        self.points_captain = points_captain or 0
        self.winner_month = winner_month or 0
        self.max_position_month = max_position_month or 0
        self.min_position_month = min_position_month or 0
        self.cost_transfer = cost_transfer or 0
        self.winner_week = winner_week or 0
        self.lost_week = lost_week or 0
        self.cant_used_player = cant_used_player or 0
        self.weeks = weeks
        self.players = players

    def __str__(self):
        # Convertir la lista de semanas en una cadena formateada
        weeks_str = "\n".join(
            [f"Fecha {week['Week']}, puntos: {week['Points']}, banco: {week['Bench']}, costo transfer: {week['Cost']}" for week in
             self.weeks])

        # Convertir la lista de jugadores en una cadena formateada
        players_str = "\n".join([
                                    f"Nombre: {player['Name']}, Partidos en el equipo: {player['Matchs']}, Puntos: {player['Points']}, Veces seleccionado capitán: {player['Capitan']}"
                                    for player in self.players])

        # return f"Equipo: {self.equipo}\nManager: {self.manager}\nFecha con más puntos: {self.max_point_fecha}, puntos realizados: {self.max_point_pts}\nFecha con menos puntos: {self.min_point_fecha}, puntos realizados: {self.min_point_pts}\nPuntos en el banco: {self.points_bench}\nPuntos de capitán: {self.points_captain}\nWinnerMonth: {self.winner_month}\nMaxPositionMonth: {self.max_position_month}\nMinPositionMonth: {self.min_position_month}\nCostTransfer: {self.cost_transfer}\nWinnerWeek: {self.winner_week}\nLostWeek: {self.lost_week}\nWeeks:\n{weeks_str}\nPlayers:\n{players_str}"
        return f"-------------------------------------------------\nEquipo: {self.equipo}\nManager: {self.manager}\nFecha con más puntos: {self.max_point_fecha}, puntos realizados: {self.max_point_pts}\nFecha con menos puntos: {self.min_point_fecha}, puntos realizados: {self.min_point_pts}\nPuntos en el banco: {self.points_bench}\nPuntos de capitán: {self.points_captain}\nCosto en transfers: {self.cost_transfer}\nJugadores utilizados: {self.cant_used_player}\nSemanas ganadas: {self.winner_week}\nSemanas último: {self.lost_week}\nFechas:\n{weeks_str}\nJugadores:\n{players_str}"