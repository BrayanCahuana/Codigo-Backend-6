#Las excepciones son formas de evitar que nuestros programas se crasheen y que siga el programa
from typing import final

#

#finally = no le importa si todo salio bien o mal igual se ejecuta
# try:
#     print(10/0)
# finally :
#     print("opps me ejecuto de todos modos")

#else = este se ejecutara cuando la operacion es exitosa
try:
    print(10/0)
except:
    print(" salio mal")
else:
    print("salio bien")

numeros = []
for numero in range(0,4):
    input ("ingrese numero: ")
try:
    numeros.append(numero)
    if numeros == str :
        print("no es correcto")
    else:
        print("ta bien")
finally:
    print(f"los datos lasieron bien son {numeros}")
