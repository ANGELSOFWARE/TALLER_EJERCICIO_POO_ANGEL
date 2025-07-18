class Animal:
    def __init__(self, idAnimal, edad, peso):
        self.idAnimal = idAnimal
        self.edad = edad
        self.peso = peso

    def alimentar(self):
        print(f"Animal {self.idAnimal} alimentado")

    def vacunar(self):
        print(f"Animal {self.idAnimal} vacunado")

    def registrarPeso(self):
        print(f"Peso del animal {self.idAnimal} registrado")
