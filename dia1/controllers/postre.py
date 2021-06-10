#un controlador es el comportamiendto que va a tener mi API cuando se llame la ruta
#/postres GET = muestra los postres

# from typing_extensions import Required
from flask_restful import Resource, reqparse
from models.postre import PostreModel
from config.conexion_bd import base_de_datos

serializerPostres = reqparse.RequestParser(bundle_errors=True)
serializerPostres.add_argument(
    'nombre',
    type = str,
    required = True,
    help="falta el nombre",
    location='json'
)
serializerPostres.add_argument(
    'porcion',
    type = str ,
    required=True,
    help="Falta la porcion",
    choices= ('Familiar','Personal'),
    location='json'
)
class PostresController (Resource) :
    def get(self):
        postres = PostreModel.query.all()
        resultado =[]
        for postre in postres:
            print(postre.json())
            resultado.append(postre.json())
        return {
            'success': True,
            'content': resultado ,
            'message': None
        }


    #POST para añadir un postre
    def post(self):
        data = serializerPostres.parse_args()
        nuevoPostre = PostreModel(nombre=data.get('nombre'),porcion=data.get('porcion'))
        print(nuevoPostre)
        nuevoPostre.save()

        return {
            'success': True,
            'content': nuevoPostre.json(),
            'message': 'Postre creado'
        },201

class PostreController(Resource):
    def get(self, id):
        otro_postre = base_de_datos.session.query(PostreModel).filter_by(postreId=id).first()
        # postre = PostreModel.query.filter_by(postreId=id).first()
        # print(postre)
        print(otro_postre)
        return {
            'success': True,
            'content': otro_postre.json(),
            'message': None
        } if otro_postre else {
            'no hay el postre'
        },404
    

    #PUT para actualizar el postre
    def put (self, id):
        postre = base_de_datos.session.query(PostreModel).filter_by(postreId = id).first()
        if postre:
            data = serializerPostres.parse_args()
            postre.postreNombre = data.get('nombre')
            postre.postrePorcion = data.get ('porcion')
            postre.save()
            return{
                'succeess' : True,
                'content' : postre.json(),
                'message' : 'postre actualizado correctamente'
            },201
        else:
            return{
                'succeess' : False,
                'content' : None,
                'message' : 'postre no encontrado'
            },404
    

    #DELETE para borrar el postre
    def delete(self, id):
        postre = base_de_datos.session.query(PostreModel).filter_by(postreId = id).first()
        if postre:
            postre.delete()
            return{
                'succeess' : True,
                'content' : None,
                'message' : 'postre no existe'
            }
        else:
            return {
                'succeess' : False,
                'content' : None,
                'message' : 'postre no existe'
            }
            
class BusquedaPostre(Resource):
    serializerBusqueda = reqparse.RequestParser()

    serializerBusqueda.add_argument(
        'nombre',
        type=str,
        location='args',
        required=False,
    )

    serializerBusqueda.add_argument(
        'porcion',
        type = str, 
        location = 'args',
        required = False,
        choices= ('Familiar','Personal'),

    )
    

    def get(self):
        filtros =self.serializerBusqueda.parse_args()
        if filtros.get('nombre') and filtros.get('porcion'):
            resultado = base_de_datos.session.query(PostreModel).filter_by(
            postreNombre = filtros.get('nombre'),postrePorcion = filtros.get ('porcion')).all()
            print(resultado)
            return 'ok'

        elif filtros.get ('nombre'):
            resultado = base_de_datos.session.query(PostreModel).filter_by(
            postreNombre = filtros.get('nombre')).all()
            print(resultado)
            return 'ok'

        elif filtros.get ('porcion'):
            resultado = base_de_datos.session.query(PostreModel).filter_by(
            postreNombre = filtros.get('porcion')).all()
            print(resultado)
            return 'ok'

        else:
            return {
                'message' : 'Necesitas dar almenos u parametro'
            }
