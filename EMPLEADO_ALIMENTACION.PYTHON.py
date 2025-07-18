from empleado import Empleado

class EmpleadoAlimentacion(Empleado):
    def __init__(self, idEmpleado, nombre, tipoAlimento):
        super().__init__(idEmpleado, nombre, "Alimentacion")
        self.tipoAlimento = tipoAlimento

    def registrarAlimentacion(self):
        print("Alimentación registrada")
