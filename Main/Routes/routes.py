from Main.api.coopapi import Coopapi #, Coopapi_coopid, Coopapi_leaderid, Coopapi_memberid, Coopsapi
from Main.api.userapi import UserApi, UsersApi
from Main.api.authapi import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/user/<uid>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(Coopapi,'/api/coop')
    #api.add_resource(Coopapi_coopid,'/api/coop/<Coopid>')
    #api.add_resource(Coopapi_memberid,'/api/coop/member/<Member_id>/<Coop_id>')