from empleado import Empleado

class EmpleadoSanidad(Empleado):
    def __init__(self, idEmpleado, nombre, especialidad):
        super().__init__(idEmpleado, nombre, "Sanidad")
        self.especialidad = especialidad

    def aplicarVacuna(self, animal, vacuna):
        print(f"Vacuna {vacuna.nombre} aplicada a {animal.idAnimal}")

    def realizarChequeo(self):
        print("Chequeo de sanidad realizado")
