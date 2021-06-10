from models.postre import PostreModel
from models.preparacion import PreparacionModel
from flask_restful import Resource, reqparse
from config.conexion_bd import base_de_datos


serializerPreparacion = reqparse.RequestParser(bundle_errors = True)
serializerPreparacion.add_argument(
    'orden',
    type = int,
    required =True,
    help = 'Flata el orden',
    location = 'json'
)
serializerPreparacion.add_argument(
    'descripcion',
    type = str,
    required = True,
    help = 'Falta la descripcion',
    location = 'json'
)
serializerPreparacion.add_argument(
    'postre_id',
    type = int,
    required = True,
    help = 'Falta el postre_id',
    location = 'json'
)


def validarPostre(postre_id):
    return base_de_datos.session.query(PostreModel).filter_by(postreId = postre_id).first()

class PreparacionesController(Resource):

    def post(self):
        data = serializerPreparacion.parse_ags()
        nuevaPreparacion = PreparacionModel(data.get('orden'),data.get('descripcion'),data.get('postre_id'))
        if validarPostre(postre_id=data.get('postre_id')):
            nuevaPreparacion.save()
        
            return {
                'success' : True,
                'content' : nuevaPreparacion.json(),
                'message' : "preparacion creada ",
            },201
            
        else:
            return {
                "success" : False,
                "content" : None,
                "message" : "postre no exisste"
        },400


    def get(self):
        pass