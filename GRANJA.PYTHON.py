class Granja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.corrales = [] 

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Se ha contratado a {empleado.nombre} como {empleado.cargo}.")

    def agregar_corral(self, corral):
        self.corrales.append(corral)
        print(f"Se ha añadido el corral {corral.id_corral} ({corral.tipo}) a la granja {self.nombre}.")

    def supervisar_granja(self):
        print(f"--- Supervisión de la granja {self.nombre} ---")
        print(f"Empleados contratados: {len(self.empleados)}")
        for emp in self.empleados:
            print(f"{emp.nombre} - {emp.cargo}, Horas trabajadas: {emp.horas_trabajadas}")

        print(f"Corrales en la granja: {len(self.corrales)}")
        for corral in self.corrales:
            print(f"Corral {corral.id_corral}: Tipo {corral.tipo}, Capacidad {corral.capacidad_maxima}, Animales: {len(corral.animales)}")
        print("--------------------------------------------")
