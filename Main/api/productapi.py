from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Product import Product
from Main.Model.Coop import Coop
from Main.Model.User import User
from Main.Model.ProductCoopDetails import product_coop_details as productcoopdetails
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity


class Productapi(Resource):
    #get all products  created by the leader
    @jwt_required
    def get(self):
        LeaderId = get_jwt_identity()
        Leader = User.objects.get(UID = LeaderId)
        Product_coop = productcoopdetails.objects.filter(Createdby__in = [Leader.id])
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


class Product_api(Resource):
    #get all products from all coops
    def get(self):
        Product_coop = productcoopdetails.objects()
        leng = len(Product_coop)
        data = {}
        for i in range(leng):
            value = "Product" + str(i)
            data[value] = {
                'Product Id': str(Product_coop[i].Product.id),
                'Product Name':Product_coop[i].Product.Name,
                'Coop' : Product_coop[i].Coop.Name,
                'Created by':Product_coop[i].Createdby.username,
                'Contact' :Product_coop[i].Createdby.mobile,
                'Description':Product_coop[i].Product.Description,
                'Quantity Available' : Product_coop[i].Product.Quantity,
                'Price':Product_coop[i].Product.Price,
            }
        return jsonify(data)
    
    
class Productapi_quantity(Resource):
    #update quantity of product
    def put(self,productId,quantity):
        try:
            product = Product.objects.get(id = productId).update(Quantity = quantity)
            return {"Response": "Product quantity updated to " + quantity},200
        except:
            return {'Response':"Record Not Found"}

class Productapi_price(Resource):
    #update price of a product
    def put(self,productId, price):
        try:
            Product.objects.get(id = productId).update(Price = price)
            return {"Response": "Product price updated to " + price},200
        except: 
            return {'Response':"Record Not Found"}
