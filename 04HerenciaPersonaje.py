class Personaje:
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.herramienta =herramienta
class Mago(Personaje):
    pass
hechicero = Mago("Merlín","caldero")

class Sa(Mago):
    pass
vida=Sa("Loca","Mal")

print(hechicero.nombre)
print(hechicero.herramienta)
print(vida.nombre)
print(vida.herramienta)
