class Corral:
    def __init__(self, idCorral, capacidad, estado):
        self.idCorral = idCorral
        self.capacidad = capacidad
        self.estado = estado
        self.animales = []

    def limpiar(self):
        print(f"Corral {self.idCorral} limpiado")

    def asignarAnimal(self, animal):
        self.animales.append(animal)

    def verificarEstado(self):
        print(f"Estado del corral {self.idCorral}: {self.estado}")
