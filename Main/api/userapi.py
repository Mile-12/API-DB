from flask import Flask, Response, request
from flask_mongoengine import json
from Main.Model.User import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json

class UsersApi(Resource):
  def get(self):
    con = User.objects().to_json()
    users = json.loads(con)
    print(users[0]["username"])
    return Response(con, mimetype="application/json", status=200)
  @jwt_required
  def post(self):
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)}, 200
 
class UserApi(Resource):
  @jwt_required
  def put(self, uid):
    body = request.get_json()
    User.objects.get(UID=uid).update(**body)
    return '', 200
  @jwt_required
  def delete(self, uid):
    user = User.objects.get(UID=uid).delete()
    return '', 200

  def get(self, uid):
    users = User.objects.get(UID=uid).to_json()
    return Response(users, mimetype="application/json", status=200)
    
