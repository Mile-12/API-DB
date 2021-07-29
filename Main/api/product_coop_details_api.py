from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Product import Product
from Main.Model.Coop import Coop
from Main.Model.User import User
from Main.Model.ProductCoopDetails import product_coop_details as productcoopdetails
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

    
class Productapi_Coopid(Resource):
    #get all products of a coop
    def get(self,coopid):
        coop = Coop.objects.get(Coopid = coopid)
        Product_coop = productcoopdetails.objects.filter(Coop__in = [coop.id])
        leng = len(Product_coop)
        data = {}
        for i in range(leng):
            value = "Product" + str(i)
            data[value] = {
                'Product Id': str(Product_coop[i].Product.id),
                'Product Name':Product_coop[i].Product.Name,
                'Created by':Product_coop[i].Createdby.username,
                'Description':Product_coop[i].Product.Description,
                'Quantity Available' : Product_coop[i].Product.Quantity,
                'Price':Product_coop[i].Product.Price,
            }
        return jsonify(data)
              
    #add a new product by auth user
    @jwt_required()
    def post(self,coopid):
        body = request.get_json()
        LeaderId = get_jwt_identity()
        product = Product(**body).save()
        Leader = User.objects.get(username = LeaderId)
        coop =  Coop.objects.get(Coopid = coopid)
        productcoopdetails(Createdby = Leader,Coop = coop,Product = product).save()
        return {'Response:':'product added successfully'},200
    
class Productapi_productid(Resource):  
    @jwt_required()
    def delete(self,productid,coopid):
        try:
            coop = Coop.objects.get(Coopid = coopid)
            product = Product.objects.get(id=productid)
            Name = product.Name
            LeaderId = get_jwt_identity()
            Createdby = User.objects.get(username = LeaderId)
            productcoopdetails.objects.filter(Product__in = [productid],Createdby__in = [Createdby.id],Coop__in = [coop.id]).delete()
            product.delete()
            return {'Response:': Name + ' has been remove successfully'},200

        except:
            return {'Response':'Record Not Found'} 
