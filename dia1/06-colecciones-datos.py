#listas
colores= ["azul","negro","amarillo"]
misc = ["eduardo",18,False,14]

#imprimir la primera poscion
print(colores[1])

#imprimir la ultima posicion
print(colores[len(colores)-1])
print(colores[-1])

#imprimir 0 hasta la < 2
print(colores[0:2])

#imprimir desde la 1
print(colores[1:])

colores2 = colores[:]
colores2[0]= "violeta"
print(colores)

#agregar a mi lista
colores.append("indigo")
print(colores)

#eliminar un elemento de la lista
colores.remove("azul")
print(colores)

#elimina y ademas se puede almacenar en una variable
colores_eliminados = colores.pop(0)
print(colores)
print(colores_eliminados)