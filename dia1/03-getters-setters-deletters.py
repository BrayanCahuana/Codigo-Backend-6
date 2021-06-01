class Electrodomesticos:
    def __init__(self):
        self.__nombre = ''
        self.__color = ''
        self.__peso = 0

    def __setNombre(self, nombre):
        """el setter sirve para definir un atributo de una forma mass formal"""
        self.__nombre = nombre
    
    def __getNombre(self):
        """El getter sirve para reotrnar el valor del atributo privado"""
        return self.__nombre
    
    def __delteNombre(self):
        """El deleter para borrar ese atributo de  la instancia de la clase"""
        del self.__nombre
    
    nombre = property(__getNombre, __setNombre, __delteNombre)

objElectrodimesticos = Electrodomesticos()
objElectrodimesticos.nombre = "Licuadora"
print(objElectrodimesticos.nombre)
del objElectrodimesticos.nombre
