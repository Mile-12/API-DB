from flask import jsonify
from Main.Model.UserCoopDetails import user_coop_details as usercoopdetails
from flask_restful import Resource
from Main.Model.User import User
from Main.Model.Coop import Coop

class User_coop_details_api(Resource):
    def get(self, uid):
        ''' Getting a list of Co-ops a user is part of '''
        user = User.objects.get(UID=uid)
        c = usercoopdetails.objects.filter(User__in = [user.id])
        leng = len(c)
        data = {}
        for i in range(leng):
            value = "Co-op" + str(i)  
            data[value] = {
            'User id' : c[i].User.UID,
            'Coop id' : c[i].Coop.Coopid,
            'Coop name' : c[i].Coop.Name,
            'Status' : c[i].Status
            }
        
        return jsonify(data)     


