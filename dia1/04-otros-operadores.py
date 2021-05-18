#Operadores de comparacion
# == es igual que 
# !=
# <
# >
# <=
# >=

numero, numero2 = 10,20
print(numero < numero2)
#if(persona<18 // nacionalidad == "venezolana"){
#    ...
#}


#Operadores logicos
#AND (en JS es &&) = sirve para validar que las dos condiciones sean verdaderas
#OR (en JS es //) = sirve para validar que almenos uande las condiciones es verdadero
#NOT (en JS es !) = sirve para que sea negativo
  
print ((10>5) and (10<11))
print ((10 >= 20)and(10<9))
print (not(10>=10) or (10>20))

#Operadores de Identidad
#is = es
#is not = no es
#sirve para ver si estan apuntando a la misma direccion de memoria

frutas = ["manzana","pera"]
frutas2 = frutas
print (frutas is frutas2)

#2 tipos de variables = variables MUTABLES y INMUTABLES
#MUTABLE: cuando nosotros hacemos una copia de esa variable, la copia se esta alojando en el mismo espacio de memoria
#INMUTABLE: es cuando hacemos una copia se alojara en otra posicion de memoria

nombres = ["eduardo","raul","carlos","estefani"]
nombres_alumnos = nombres
nombres_alumnos[0] = ["carmen"]
nacionalidad ="peuano"
nacionalidad2 = nacionalidad
nacionalidad2 = "brazileña"
print (nacionalidad)
print(nombres)
print (nacionalidad is nacionalidad2)
print (nombres is nombres_alumnos)
#sirve para poder ubicar en cual esta la variable
print(id(nombres))
print (hex(id(nombres)))
