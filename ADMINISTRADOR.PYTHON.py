from empleado import Empleado

class Administrador(Empleado):
    def __init__(self, idEmpleado, nombre):
        super().__init__(idEmpleado, nombre, "Administrador")

    def supervisarCorrales(self):
        print("Supervisando corrales")

    def registrarAsistencia(self):
        print("Administrador registró asistencia")

    def generarReportes(self):
        print("Administrador generando reportes")
