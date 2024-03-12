class Equipo:
    def __init__(self, codigo, nombre, manager):
        self.codigo = codigo
        self.nombre = nombre
        self.manager = manager

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Manager: {self.manager}"