from flask import Flask, Response, request
from flask_mongoengine import json
from Main.Model.Coop import Coop
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json

class Coopapi(Resource):
    def get(self):
        coop = Coop.objects().to_json() 
        return Response(coop,mimetype="application/json",status=200)

    @jwt_required
    def post(self):
        #create new coop
        body = request.get_json()
        coop = Coop(**body).save()
        id = coop.Coopid
        #update leader field of the coop
        LeaderId = get_jwt_identity()
        Leader = User.objects.get(UID = LeaderId) 
        coop.update(push__Leader = Leader)
        #update coop list of Leader
        Leader.update(push__coopL = coop)
        return {'coopid:': str(id)}, 200
    
'''
to manipulate coop table with coopid 
'''
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
        Leader.update(pull__coopL = coop)
        coop.delete()
        return '',200

'''Add or remove Member from coop'''
class Coopapi_memberid(Resource): 
    def post(self, Member_id,Coop_id):
        coop = Coop.objects.get(Coopid =Coop_id)
        member = User.objects.get(UID = Member_id)
        coop.update(push__Members = member)
        return '',200

    def delete(self,Member_id,Coop_id):
        coop = Coop.objects.get(Coopid =Coop_id)
        member = User.objects.get(UID = Member_id)
        coop.update(pull__Members = member)
        return '',200

'''add or remove Product'''