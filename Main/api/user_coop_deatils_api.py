from flask import jsonify
from Main.Model.UserCoopDetails import user_coop_details as usercoopdetails
from flask_restful import Resource
from Main.Model.User import User
from Main.Model.Coop import Coop

class User_coop_details_api(Resource):
    def get(self, username):
        ''' Getting a list of Co-ops a user is part of '''
        user = User.objects.get(username=username)
        c = usercoopdetails.objects.filter(User__in = [user.id])
        leng = len(c)
        data = {}
        for i in range(leng):
            value = "Co-op" + str(i)  
            data[value] = {
            'User name' : c[i].User.username,
            'Coop id' : c[i].Coop.Coopid,
            'Coop name' : c[i].Coop.Name,
            'Status' : c[i].Status
            }
        
        return jsonify(data)     

class Users_in_coop_api(Resource):
    def get(self, cid):
        ''' Getting a list of Co-op's  Members  '''
        coop = Coop.objects.get(Coopid=cid)
        c = usercoopdetails.objects.filter(Coop__in = [coop.id])
        leng = len(c)
        data = {}
        for i in range(leng):
            value = "Member" + c[i].User.username  
            data[value] = {
            'Member name' : c[i].User.username,
            }
        return jsonify(data)     

