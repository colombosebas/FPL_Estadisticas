class Club:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}"