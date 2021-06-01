from flask import Flask, request
from flask_cors import CORS

#__name__ muetra si el archivo en el cual se esta llamando a la clase flask es el archivo principal del proyecto, para evitar que la instancia de la clase Flask se puede crear varias veces
#si estamos en el archivo principal nos imprimira __main__  , caso contrario nos imprime otra cosa

app = Flask(__name__)
CORS(app, methods=['GET','POST'], origins = ['*'])
productos = []

#Un decorador es un patron de sowftware que se utiliza para modificar el funcionamiento de una funcion o clase en particular sin necesidad de emplea otros metodos como herencia
@app.route("/")
def inicio():
    print("me llamaron")
    return("hola mundo")

@app.route("/productos",methods=['GET','POST'])
def gestion_de_productos():
    print(request.method)
    #request.get_json()   podemos ver la informacion que me esta brindando el frontend mediante el body
    request.get_json()

    #si el metodo es post indicar ne el message "producto creado exitosamente"
    # si el metodo es get indircar el mensage "estos so lo productos"

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        productos.append(data)
        return{
            "message":"producto creado",
            "productos": data },201

    else:
        return{
            "Producto": "registrados",
            "Content": productos
        }
#al hacer un get queda prohibido enviar informacion mediante el body
# @app.route("/productos/<int:id>",methods =(['PUT','DELETE','GET']))
# def gestion_pructos (id):
#     print(id)
#     return "ok"

@app.route("/productos/<int:id>")
def posicion ():
    data = request.get_json()
    if posicion == "" :
        return {}, 404
    else:
        return {data}, 200



@app.route("/productos/buscar")
def buscar_productos():
    print(request.args.get("nombre"))
    return "ok"

#debug=True cada vez que hagamos un cambio y lo guademos automaticamete se einiciara mi servidor con los nuevos cambios
app.run(debug=True)
#NOTA!: todo codigo que pongmos despues del metodo run nuca se ejecutara , porque el metodo run()
#hace que se quede colgado mi programa levantando mi servidor
