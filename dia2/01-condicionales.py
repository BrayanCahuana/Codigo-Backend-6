#Metodo para ingresar datos por la terminal
#edad = input("ingresa tu edad /n")
#print(type(edad))

#Para convertir datos
#edadEntero = int(edad)
#print(type(edadEntero))

#edad = int(input("ingresa otra vez: /t"))
#print(float(10))

#CONDICION
#If (si) ,        ELSE (sino haz este otro) ,       ELIF(SINOSI)
#

#restricion_edad = 80
#if restricion_edad >= 18 and restricion_edad <65:
 #   print("puedes tomar alcohol")
#elif restricion_edad >= 65:
 #   print("jubilate")
#else :
 #   print("piña, esperate :v")


#OPERADOR TERNARIO
#respuesta = "eres mayor" if (restricion_edad >= 18) else "eres menor"
#print (respuesta)


#numero = int(input("ingresa numero"))
#if numero > 0 :
  #  print("es positivo")
#elif numero == 0 : 
 #   print("es cero")
#elif numero < 0 :
  #  print("negativo")


#BUCLE
#FOR = repite desde hasta , es un bucle con inicio y fin

meses = ["enero","febrero","marzo"]
for mes in meses:
    print(mes)
for numero in range (1,10):
    print (numero)

#for tambien sirve para iterar todas las colecciones de datos
diccionario ={
    "nombre" : "eduardo",
    "apellido" : "martinez"
}
 #for (dato,valor) in diccionario:
   # print(diccionario[llave])

#break = hace que el buvle finalice
for i in range(10):
    print(i)
    if i == 5:
        break

#continue = salta la iteracion actual y no permite que el resto del codigo se ejecute

for i in range(10):
    if i ==5:
        continue
    print(i)

# # dados los siguientes numeros
# numeros = [1, 2, 5, 9, 12, 15, 10, 34, 867, 67]
# # indicar cuantos de ellos son multiplos de 3 y de 5, ademas, si hay un multiplo de 3 y de 5 no contabilizarlo
# for i in numeros:
#     if numeros == 5:
#         print("es multiplo de 5")
#     else:
#         print("es multipo de 3")

#WHILE (mientras)
edad = 25
while edad > 18 :
    print (edad)
    edad -=1

# ingresar por teclado 3 nombres y de acuerdo a ello indicar cuantos pertenecen a la siguiente lista de personas inscritas
inscritos = ["raul", "pedro", "maria", "roxana", "margioret"]
for nombre in range(1,4):
    nombres = input("ingresa nombre:  ")
    if nombres in inscritos[:] :
        print("en lista")
    else:
        print("no esta en lista")