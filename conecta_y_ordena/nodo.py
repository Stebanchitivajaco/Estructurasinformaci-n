class Nodo:
    """Representa un animal rescatado dentro del sistema."""

    def __init__(self, id_animal, nombre, especie, edad):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.estado = "en_espera"
        self.anterior = None
        self.siguiente = None