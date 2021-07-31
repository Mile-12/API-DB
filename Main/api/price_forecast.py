from flask import request
from Main.Model.User import User
from flask_restful import Resource
from flask import Response, request
from config import Config
import requests

from datetime import date

class PriceAPI(Resource):
 def post(self):
    to_date = date.today()
    body = request.get_json()
    print(body)
    API_KEY = Config.IBM_API
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    # {"input_data": [{"fields": ["date","main_commercial_species","size"],"values": [["2021-01-01","Rey",5]]}]}
    payload_scoring = body
    response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/06f02801-afa6-4ba9-bb1d-a348636a7963/predictions?version=2021-07-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    data = response_scoring.json()
    return {"price EURO" :data['predictions'][0]['values'][0][0]}