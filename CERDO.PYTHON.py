from animal import Animal

class Cerdo(Animal):
    def __init__(self, idAnimal, edad, peso, grasaCorporal):
        super().__init__(idAnimal, edad, peso)
        self.grasaCorporal = grasaCorporal

    def controlPeso(self):
        print("Peso del cerdo controlado")
