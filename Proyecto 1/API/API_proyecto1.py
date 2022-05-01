from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from proyecto1_deployment import transformar

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Predicción del precio de un automovil',
    description='Predicción del precio de un automovil')

ns = api.namespace('predict', 
     description='Predicción precio')

parser = api.parser()

parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help='Año del modelo del vehículo', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=int, 
    required=True, 
    help='Número de millas', 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='Estado (USA) en el que el vehículo está listado', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Marca del vehículo', 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='Modelo del vehículo', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PrediccionApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": transformar(args)  
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)