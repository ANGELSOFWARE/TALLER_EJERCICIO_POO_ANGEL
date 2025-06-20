class Corral:
    def __init__(self, id_corral, tipo, capacidad_maxima):
        self.id_corral = id_corral
        self.tipo = tipo  
        self.capacidad_maxima = capacidad_maxima
        self.animales = []  

    def asignar_animal(self, animal):
        if len(self.animales) < self.capacidad_maxima:
            self.animales.append(animal)
            print(f"{animal._nombre} ha sido asignado al corral {self.id_corral} ({self.tipo}).")
        else:
            print(f"No hay espacio en el corral {self.id_corral} para {animal._nombre}.")
    
    def limpiar(self):
        print(f"El corral {self.id_corral} ha sido limpiado.")
