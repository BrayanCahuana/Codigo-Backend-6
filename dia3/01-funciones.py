#es un bloque de codigo que se utiliza varias veces

numero1 = 10
numero = 20

sumatoria = 1 + 2


def saludar ():
    """Funcion que te saluda"""
    print ("hola amigos de codigo")

print ("ya es tarde")
saludar ()


#Las funciones tambien pueden definir variables que solo se ejecuta dentro de la misma

# def saludarConNombre(nombre):
#     """Funcion que recibe el nombre y lo imprime"""
#     print(f"hola{nombre} buenas tardes")
#     print(f"hola{nombre}")

# saludarConNombre(input("pon tu nombre:  \n \t"))

def saludoOpcional(persona = None):
    print(f"hola {persona}")

    saludoOpcional(" yo ps")
    saludoOpcional()

#si queremos recibir parametros obligatoriamente y algunos opcionalemte, los parametros opcionales siempre tienen que ir al final de la declaracion
def registro (correo, nombre = None ):
    print("registro exitoso")

registro ("yodsaddsa")

# funcion que reciba dos numeros y si la sumatoria de ambos es par indicar su mitad y si es impar, retornar el resultado de la sumatoria
def funcion (numero1, numero2):
    sumatoria = numero1 + numero2
    if sumatoria % 2 == 0:
        print(f"sumatoria es {sumatoria} y la mitad es: ")
        print(sumatoria /2)
    else:
        print(f"sumatoria es la siguiente:{sumatoria}")

funcion (0,1)
#parametro *args es una lista dianmoca de elementos para recibir un numero ilimitado de valores

def inscritos (*argumentos):
    print(argumentos)

inscritos("eduardo","Carlos","Gmalia")



# for lista in range(2):
#     lista = input("ingresa nombre")
# if lista == "carlos":
#     print("aaa")
# else:
#     print("eeee")

def tareas(nombre, *args):
    print(nombre)
    print(args)
tareas("tarea","crean un archivo python")


# definir una funcion para que reciba una N cantidad de alumnos y que indique cuantos fueron aprobados y cuandos desaprobaron



def alumnos(*cantidad):
    aprobados = 0
    desaprobados = 0
    for alumno in cantidad:
        print(alumno["nota"])
        if alumno["nota"] > 11:
            aprobados += 1
        else:
            desaprobados += 1
    print(f"aprobados{aprobados} y desaprobados{desaprobados}")


alumnos({"nombre": "Eduardo", "nota": 7},
        {"nombre": "Fidel", "nota": 16},
        {"nombre": "Raul", "nota": 18},
        {"nombre": "Marta", "nota": 20},
        {"nombre": "Juliana", "nota": 14},
        {"nombre": "Fabiola", "nota": 16},
        {"nombre": "Lizbeth", "nota": 15})

#keywoord argument = **kwargs sirve para pasar un numero indeterminado de parametros pero tenemos que definir el nombre del parametro

def indeterminada(**kwargs):
    print(kwargs)

indeterminada (nombre = "Eduardo", apellido = "Rivero")
indeterminada (nombre = "maria", apellido = "peres")
indeterminada (edad = 16, nota = 18)


kwargs = 0
def mifuncion(*args,**kwagrs):
    print(args)
    print(kwargs)
    
mifuncion(10,"maria")

def multiplicacion(numero1,numero2):
    return numero1 * numero2 ,100

    