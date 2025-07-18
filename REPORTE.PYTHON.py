class Reporte:
    def __init__(self, tipo, fecha, contenido):
        self.tipo = tipo
        self.fecha = fecha
        self.contenido = contenido

    def generar(self):
        print("Reporte generado")
