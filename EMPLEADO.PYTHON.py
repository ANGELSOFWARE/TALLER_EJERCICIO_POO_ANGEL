class Empleado:
    def __init__(self, idEmpleado, nombre, cargo):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.cargo = cargo

    def realizarTarea(self):
        print(f"{self.nombre} realizando tarea")

    def registrarAsistencia(self):
        print(f"{self.nombre} registró asistencia")

    def reportarIncidencias(self):
        print(f"{self.nombre} reportó incidencias")
