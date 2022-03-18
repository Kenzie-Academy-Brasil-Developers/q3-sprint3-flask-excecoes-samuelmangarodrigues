import json
from json import JSONDecodeError
from telnetlib import STATUS
import os
from flask import jsonify, request


def reader_users() -> list:
    try:
        with open('./app/database/database.json','r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        os.system('touch ./app/database/database.json')
        with open('./app/database/database.json','a') as json_file:
           json.dump([],json_file)
           return []
    except JSONDecodeError:
        with open('./app/database/database.json','a') as json_file:
            json.dump({"data":[]},json_file)
            return {'data':[]}

        
def write_users(payload:dict):
    json_data=reader_users()
   
    if json_data['data'] == []:
       id=1
       
    else:
        final=json_data['data'][-1]['id']
        id=final+1
   
    if type(payload['nome']) !=str and type(payload['email'])!=str:
        return {'error':'type nome and email wrong'}

    if type(payload['email'])!=str:
        return {'error':'type email wrong'}
        
    if type(payload['nome']) !=str:
        return {'error':'type nome wrong'}

    for dici in json_data['data']:
        if dici['email']==payload['email']:
            return {"error": "User already exists."}
        dici['nome'] = dici['nome'].title()
        dici['email'] = dici['email'].lower()
    payload['id']=int(id)
    jsonify(json_data['data'].append(payload))


    with open('./app/database/database.json','w') as json_file:
        json.dump(json_data,json_file,indent=2)


        return payload 


def add_id():
    data_body=request.get_json()  
    data=reader_users()


    for dici in data['data']:
        print(dici['nome'])
    return ''