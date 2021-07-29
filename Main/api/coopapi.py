from flask import Flask, Response, request, jsonify
from flask_mongoengine import json
from Main.Model.Coop import Coop
from Main.Model.User import User
from Main.Model.UserCoopDetails import user_coop_details as usercoopdetails
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

class Coopapi(Resource):
    def get(self):
        coop = Coop.objects().to_json() 
        return Response(coop,mimetype="application/json",status=200)
    
    @jwt_required()
    def post(self):
        #create new coop for the auth user
        body = request.get_json()
        LeaderId = get_jwt_identity()
        Leader = User.objects.get(username = LeaderId)
        coop = Coop(**body).save()
        usercoopdetails(User = Leader, Coop = coop, Status = "Leader" ).save() 
        # this will add the User , coop and give leader status to the user
        return {'Response:': 'added sucessfully'}, 200



