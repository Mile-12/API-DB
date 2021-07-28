from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Profit import Profit
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

class Profit_level(Resource):
    #add profit 
    def post(self, coopid):
        try:
            body = request.get_json()
            body.update({'Coopid': coopid})
            Profit(**body).save()
            return {'Response:': 'Profit added'}, 200
        except: 
            return {'Response':"error adding record"}

    #get profit history of a coop
    def get(self, coopid):
        try:
            profit = Profit.objects.filter(Coopid=coopid)
            leng = len(profit)
            data = {}
            for i in range(leng):
                value = str(i+1)
                data[value] = {

                    'Month': profit[i].Month,
                    'Week': profit[i].Week,
                    'Year': profit[i].Year,
                    'Profit': profit[i].Profit
                }
            return jsonify(data)
        
        except:
            return {'Response':"Record Not Found"}
