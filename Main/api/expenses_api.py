from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Expenses import Expenses
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

class Expenses_api(Resource):
    #add expenses 
    def post(self, coopid):
        try:
            body = request.get_json()
            body.update({'Coopid': coopid})
            Expenses(**body).save()
            return {'Response:': 'Expense added'}, 200
        except: 
            return {'Response':"error adding record"}

    #get list of expenses of a coop 
    def get(self, coopid):
        try:
            expenses = Expenses.objects.filter(Coopid=coopid)
            leng = len(expenses)
            data = {}
            for i in range(leng):
                value = str(i+1)
                data[value] = {

                    'Location':expenses[i].Location,
                    'Product Name': expenses[i].ProductName,
                    'Amount':expenses[i].Amount,
                    'Date':expenses[i].Date
                }
            return jsonify(data)
        
        except:
            return {'Response':"Record Not Found"}
