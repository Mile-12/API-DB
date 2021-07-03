from flask import Flask, Response, request, jsonify
from Main.Model.UserCoopDetails import user_coop_details as usercoopdetails
from flask_restful import Resource
from Main.Model.User import User
from Main.Model.Coop import Coop
from flask_jwt_extended import jwt_required,get_jwt_identity
from multipledispatch import dispatch

class User_coop_details_api(Resource):

    def get(self):
        coop = usercoopdetails.objects().to_json() 
        return Response(coop,mimetype="application/json",status=200)
    
    def get(self, uid):
        user = User.objects.get(UID=uid)
        Coop1 = Coop.objects.get(Coopid="C-1")
        coop = usercoopdetails.objects.get(User = user,Coop1 = Coop )
        return Response(coop,mimetype="application/json",status=200)