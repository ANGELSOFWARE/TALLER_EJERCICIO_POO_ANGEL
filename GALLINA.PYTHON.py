from animal import Animal

class Gallina(Animal):
    def __init__(self, idAnimal, edad, peso, produccionHuevos):
        super().__init__(idAnimal, edad, peso)
        self.produccionHuevos = produccionHuevos

    def recolectarHuevos(self):
        print("Huevos recolectados")
