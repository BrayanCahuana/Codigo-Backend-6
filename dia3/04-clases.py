class Mueble:
    tipo=""
    valor = 00.00
    colores = []
    especificacion =[]
    def indicar_tipo (self):
        return self.tipo()
    def mostrar_especificaciones(self):
        return self.especificacion