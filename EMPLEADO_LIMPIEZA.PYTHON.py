from empleado import Empleado

class EmpleadoLimpieza(Empleado):
    def __init__(self, idEmpleado, nombre, areaAsignada):
        super().__init__(idEmpleado, nombre, "Limpieza")
        self.areaAsignada = areaAsignada

    def realizarLimpieza(self):
        print("Limpieza realizada")
