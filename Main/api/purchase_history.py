from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Product import Product
from Main.Model.Coop import Coop
from Main.Model.User import User
from Main.Model.purchaseHistory import purchase_History
from Main.Model.ProductCoopDetails import product_coop_details as productcoopdetails
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class Purchase_history(Resource):
    # get all purchase records of a coop
    #@jwt_required
    def get(self, coopid):
        try:
            History = purchase_History.objects.filter(coopid=coopid)
            leng = len(History)
            data = {}
            for i in range(leng):
                value = "Order:" + str(i+1)
                data[value] = {
                    'Product Name': History[i].ProductName,
                    'Price:': History[i].Price,
                    'Quantity': History[i].Quantity,
                    'Sold to': {
                        'Name': History[i].CustomerName,
                        'contact': History[i].CustomerContact
                    }
                }
            return jsonify(data)
        
        except: 
            return {'Response':"Record Not Found"}
    # add a new Purchase History

    def post(self, coopid):
        try:
            body = request.get_json()
            body.update({'coopid': coopid})
            purchase_History(**body).save()
            return {'Response:': 'Purchase history added'}, 200
        except: 
            return {'Response':"error adding record"}
