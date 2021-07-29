from flask import jsonify
from Main.Model.UserCoopDetails import user_coop_details as usercoopdetails
from flask_restful import Resource
from Main.Model.User import User
from Main.Model.Coop import Coop
from flask_jwt_extended import jwt_required

class add_member_api(Resource):
    jwt_required()
    def post(self, username,cid):
        '''Add a user to a Co-op'''
        coop = Coop.objects.get(Coopid = cid)
        member = User.objects.get(username = username)
        usercoopdetails(User = member, Coop = coop, Status = "Member" ).save() 
        return {'Response:': str(member.username)+' has been added sucessfully to '+str(coop.Name)}, 200
    
    def delete(self, username,cid):
        ''' Remove a User from the Co-op'''
        coop = Coop.objects.get(Coopid = cid)
        member = User.objects.get(username = username)
        u = usercoopdetails.objects.filter(User__in = [member.id], Coop__in = [coop.id]).delete()
        return {'Response:': str(member.username)+' has been removed sucessfully from '+str(coop.Name)}, 200

