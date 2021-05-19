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

del colores [0]
print(colores)

#metodo para resetear la lista y dej en blanco
colores.clear()
print(colores)

#TUPLAS = colecion de elementos ordenada que no se puede modificar
notas = (14,16 ,17, 11)
print(notas[0])
print(notas[-1])
print(len(notas))
print(notas[:])

print("las notas son:{}".format(len(notas)))

#ver si hay elelmentos repetidos en una tupla
print(notas.count(2))


#CONJUNTOS = coleccion de elementos desordenada, osea que una vez que la creemos no podremos a sus posiciones ya que se ordenan aleatorio
estaciones = {"verano","otoño","invierno"}
estaciones.add("primavera")
print(estaciones)

#el metodo in sirve para invalidar si un valor esta dentro de la colecio de datos
print("primavera" in estaciones)

#DICCIONNARIOS = coleccion de elementos que estan indexados que nosotros manejamos el nombre de su llave

persona = {
    'id' : 1,
    'nombre' : "juan",
    'hobbies': [
        {
            'futbol': "basico",
        },
        {
            'voley' : "intermedio"
        },
    ]
}
print (persona ['nombre'])
print (persona ['hobbies'][0]['futbol'])



libro = {
    "nombre": "Harry Potter",
    "autor": "J.K. Rowling",
    "editorial": "Blablabla",
    "año": 2018,
    "idiomas": [
        {
            "nombre": "portuges"
        },
        {
            "nombre": "ingles",
            "nombre": "ingles britanico"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
    "tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix")
}
print(libro["año"])





# EJERCICIO 1 
# devolver el autor del libro
print(libro["autor"])

# EJERCICIO 2
# devolver el segundo tomo
print(libro["tomos"][1])

# EJERCICIO 3
# devolver la cantidad de idiomas del libro
print(len(libro["idiomas"]))

# EJERCICIO 4
# indicar si esta o no esta el idioma ruso
print(libro["idiomas"][0]["nombre"])