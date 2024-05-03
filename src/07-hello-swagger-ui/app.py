from flask import Flask, jsonify, redirect, request
from flasgger import Swagger
import logging

logger = logging.getLogger(__name__)

template = {
  "swagger": "2.0",
  "info": {
    "title": "Hello Swagger UI demo",
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
  ],
  "operationId": "getmyData"
}

app = Flask(__name__)
swagger = Swagger(app, template=template)
# swagger = Swagger(app)

@app.route('/')
def hello():
    return redirect("apidocs")

@app.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
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

@app.route('/clients/<clientid>', methods=['POST'])
def set_client(clientid):
    """Example endpoint to update a client    
    ---    
    parameters:
      - in: path
        name: clientid
        type: string
        required: true
      - name: client
        in: body
        type: json
        required: true
        value:         
        description: json object to includ sql driver settings   
    definitions:
      body:       
        type: object
        $ref: '#/definitions/client'
      client:
        type: object
        properties:
          first_name:
            type: string
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
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
      if type(request.json) != dict:
          return jsonify({'error': 'body must be a json object'}), 400
      if 'sqldriver' not in request.json:
          return jsonify({'error': 'bad json request, need to have sqldriver property'}), 400
      
      sqldriver = request.json['sqldriver']        
    
      return jsonify(sqldriver)
    except Exception as user_sampler_ex:
      print('unhandled exception at forming random user' + str(user_sampler_ex))
      return jsonify({'error': str(user_sampler_ex)}), 500    
    
@app.route('/audit/v2/sampler/<botid>', methods=['GET'])
def audit_sampler(botid):
    """endpoint returning a list of audit sample accounts from daily edit accounts    
    ---    
    parameters:
      - name: botid
        in: path
        type: string
        required: true
        value:         
        description: please enter botid      
      - name: tableId
        in: query
        type: string
        required: true
        value: 
        description: 1 == Billing_Edits(Required sample mode[0 or 1]); 2 == Billing_Assurance;3 == Billing_eRequest;
      - name: sampleMode
        in: query
        type: string
        required: false
        value: 
        description: required when tableId ==1 [0 == edits assigned to Auditors and Analysts based on their sample percentage are set; 1== edits assigned to Auditors will be assigned to Analysts]
            
    definitions:
      audit_sampler:
        type: object
        properties:
          audit_sampler:
            type: array
            items:
              $ref: '#/definitions/audit_sampler'      
    responses:
      200:
        description: A list of accounts (randomized accounts from edit inventory)
        schema:
          $ref: '#/definitions/audit_sampler'
        examples:
           {
            "botID": "d290f1ee-6c54-4b01-90e6-d701748f0851",
            "tableID": "1",
            "data": [
                {
                    "auditType": "Billing_Edits",
                    "pasCOID": "08591",
                    "sourceKeyID": "EA84DF91-BF15-E911-B73A-0025B5A0165A",
                    "assignedID": "CPU8447",
                    "firstName": "Marianne",
                    "lastName": "Marty",
                    "role": "Auditor"
                },
                {
                    "auditType": "Billing_Edits",
                    "pasCOID": "08591",
                    "sourceKeyID": "6D90DF91-BF15-E911-B73A-0025B5A0165A",
                    "assignedID": "nqe6706",
                    "firstName": "Blake",
                    "lastName": "Boerger",
                    "role": "Auditor"
                }
            ]
        }

    204:
        description: No Content is available (Returns empty if data is not available)
    400:
        description: Any error occured 
    """
        
    logger.info(f'Start audit_sampler botid: "{botid}"')
    
    value = [
                {
                    "auditType": "Billing_Edits",
                    "pasCOID": "08591",
                    "sourceKeyID": "EA84DF91-BF15-E911-B73A-0025B5A0165A",
                    "assignedID": "CPU8447",
                    "firstName": "Marianne",
                    "lastName": "Marty",
                    "role": "Auditor"
                },
                {
                    "auditType": "Billing_Edits",
                    "pasCOID": "08591",
                    "sourceKeyID": "6D90DF91-BF15-E911-B73A-0025B5A0165A",
                    "assignedID": "nqe6706",
                    "firstName": "Blake",
                    "lastName": "Boerger",
                    "role": "Auditor"
                }
            ]         
    ret = jsonify(value)
    return ret

@app.route('/audit/v2/accounts/reassignment', methods=['POST'])
def user_sampler():
    """endpoint returning a list of audit assignments for requested users    
    ---    
    parameters:
      - name: body
        in: body
        type: string
        required: true
        value:         
        description: List of accountIds and userIds need to supply to get random assignments for all accounts
    definitions:
      user_sampler:
        type: object
        properties:
          user_sampler:
            type: array
            items:
              $ref: '#/definitions/audit_sampler'      
    responses:
      200:
        description: A list of accounts (randomized accounts for requested users)
        schema:
          $ref: '#/definitions/user_sampler'
        examples:
           {
    "assignments": [
          {
              "accountId": "6AA851E0-DF19-E911-B737-00505688AFF6",
              "userId": "LUD8931"
          },
          {
              "accountId": "CEA751E0-DF19-E911-B737-00505688AFF6",
              "userId": "DWO8538"
          },
          {
              "accountId": "20A851E0-DF19-E911-B737-00505688AFF6",
              "userId": "CLO9627"
          },
          {
              "accountId": "3CA851E0-DF19-E911-B737-00505688AFF6",
              "userId": "DWO8538"
          }
      ]
    }
    
    204:
        description: No Content is available (Returns empty if data is not available)
    400:
        description: Any error occured 
    """

    logger.info('Start user_sampler')
    output_json = jsonify({ "bob": "smith"})
    try:
        
        raise "Oops WTH happened?"
    except Exception as user_sampler_ex:
        logger.error('unhandled exception at forming random user' + str(user_sampler_ex))
        return jsonify({'error': str(user_sampler_ex)}), 400
    return jsonify(output_json)

if __name__ == '__main__':
    app.run('localhost', debug=True, port=8080)