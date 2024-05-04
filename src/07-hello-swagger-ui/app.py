from flask import Flask, jsonify, redirect, request
from flasgger import Swagger
import logging

logger = logging.getLogger(__name__)

class AppConfig():
    @property
    def port_number(self) -> int:
        return 8080
    
    @property
    def localhost(self):
        return 'localhost'
    
    @property
    def debugMode(self) -> bool:
        return True

_appConfig = AppConfig()

template = {
  "swagger": "2.0",
  "info": {
    "title": "Swagger UI Demo API App",
    "description": "API for demo swagger UI",
    "contact": {
      "responsibleOrganization": "XGP Consulting Inc",
      "responsibleDeveloper": "Liran Barniv",
      "email": "lbnobs@gmail.com",
      "url": "https://www.linkedin.com/in/liranbarniv",
    },
    "termsOfService": "http://me.com/terms",
    "version": "0.0.1"
  },  
  "schemes": [
    "http",
    "https"
  ]
}

app = Flask(__name__)
swagger = Swagger(app, template=template)
# swagger = Swagger(app)

@app.route('/health', methods=['GET'])
def health():
    """Return healt check status
    ---
    tags:
      - Health
    definitions:
      HealthResponse:
        type: string        
    responses:
      200:
        description: Returns the application health status
        schema:
          $ref: '#/definitions/HealthResponse'
        examples:
          health_response:
            "i am alive:8080"

    """
    ret = f'I am alive:{_appConfig.port_number}'
    logger.info(f'Call to /health returns: "{ret}"')
    return ret

@app.route('/')
def hello():
    return redirect("apidocs")

@app.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    tags:
      - Colors

    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties: 
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


    
# example 
# host/customer/1?all=true&sampleMode=false
    
@app.route('/customer/<id>', methods=['GET'])
def sampler_get(id):
    """endpoint returning a list of audit sample accounts from daily edit accounts    
    ---    
    tags:
      - Customer
    parameters:
      - name: id
        in: path
        type: string
        required: true
        value:         
        description: please enter customer id      
      - name: all
        in: query
        type: string
        required: false
        value: 
        description: lookg through all customers or not
      - name: sampleMode
        in: query
        type: string
        required: false
        value: 
        description: sample mode true/false
            
    definitions:
      address: 
        type: object
        properties:
          street:
            type: string
            description: Street address
          city:
            type: string            
            description: City Name
      customer:
        type: object
        properties:
          first_name:
            type: string
            description: customer first name
          address:
            type: array
            items:
              $ref: '#/definitions/address'      
    responses:
      200:
        description: A list of accounts (randomized accounts from edit inventory)
        schema:
          $ref: '#/definitions/customer'
        examples:
          customer:
            {
              "first_name": "Liran",
              "address": 
                {
                  "street": "111 Washington Ave",
                  "city": "Miami",
                }
            }            

      204:
          description: No Content is available (Returns empty if data is not available)
      400:
          description: Any error occured 
    """
                
    value ={
      "customer":
        {
          "first_name": "Liran",
          "address": 
            {
              "street": "111 Washington Ave",
              "city": "Miami",
            }
        }           
    }    
    ret = jsonify(value)
    return ret

class BadRequest(BaseException): ...    

class Validate():    
    def isObj(self, obj):
      if type(obj) != dict:
        raise BadRequest('body must be a json object')
    
    def has(self, obj:dict, name: str) -> None:
      if name not in obj:
        raise BadRequest('bad json request, need to have sqldriver property')       

     
_validate = Validate()

@app.route('/customer/<id>', methods=['POST'])
def set_client(id):
    """Example endpoint to update a client    
    ---
    tags:
      - Customer
        
    parameters:
      - name: id
        in: path
        type: string
        required: true
        value:         
        description: please enter customer id      
      - name: client
        in: body
        schema:
          $ref: '#/definitions/customer'        
        type: json
        required: true        
        description: customer json object
    definitions:
      body:       
        type: object
        $ref: '#/definitions/customer'      
    responses:
      200:
        description: A list of accounts (randomized accounts for requested users)
        schema:
          $ref: '#/definitions/body'
        examples:           
        
    500:
        description: Any error occured 
    """
    logger = logging.getLogger(__name__)
    try:
      logger.info('set_sql_driver start')        
      
      _validate.isObj(request.json)
      _validate.has(request.json, "first_name")
      _validate.has(request.json, "address")
                  
      request.json['first_name'] = request.json['first_name'] + ' indeed!'
    
      return jsonify(request.json)
    
    except BadRequest as ex:
      return jsonify({'error': str(ex)}), 400      
    except Exception as ex:
      print('unhandled exception at forming random user' + str(ex))
      return jsonify({'error': str(ex)}), 500

if __name__ == '__main__':
    logger.info('Host: {_appConfig.localhost}, Debug: {_appConfig.debugMode}, Port Number: _appConfig.port_number' )               
    app.run(_appConfig.localhost, debug=_appConfig.debugMode, port=_appConfig.port_number)