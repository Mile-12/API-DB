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
        #create new coop
        body = request.get_json()
        LeaderId = get_jwt_identity()
        coop = Coop(**body).save()
        Leader = User.objects.get(UID = LeaderId)
        usercoopdetails(User = Leader, Coop = coop, Status = "Leader" ).save() 
        # this will add the User , coop and give leader status to the user
        return {'coopid:': str(id)}, 200
    
'''
to manipulate coop table with coopid 

class Coopapi_coopid(Resource):
    @jwt_required
    def put(self,Coopid):
        body = request.get_json()
        Coop.objects.get(Coopid = Coopid).update(**body)
        return '',200
    @jwt_required
    def delete(self,Coopid):
        coop = Coop.objects.get(Coopid = Coopid)
        LeaderId = get_jwt_identity()
        Leader = User.objects.get(UID = LeaderId)
        Leader.update(pull__coopL = coop.to_dbref())
        coop.delete()
        return '',200
'''

'''Add or remove Member from coop'''

'''add or remove Product'''

