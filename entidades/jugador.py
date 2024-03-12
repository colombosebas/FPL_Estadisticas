class Player:
    def __init__(self, codigo, nombre, id, posicion, club):
        self.codigo = codigo
        self.nombre = nombre
        self.id = id
        self.posicion = posicion
        self.club = club

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Id: {self.id}, Posición: {self.posicion}, Club: {self.club}"