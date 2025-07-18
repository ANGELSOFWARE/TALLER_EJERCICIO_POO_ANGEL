from animal import Animal

class Vaca(Animal):
    def __init__(self, idAnimal, edad, peso, produccionLeche):
        super().__init__(idAnimal, edad, peso)
        self.produccionLeche = produccionLeche

    def ordeñar(self):
        print("Vaca ordeñada")
