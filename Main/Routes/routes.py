from Main.api.coopapi import Coopapi 
from Main.api.add_member_api import add_member_api 
from Main.api.user_coop_deatils_api import User_coop_details_api
from Main.api.userapi import UserApi, UsersApi
from Main.api.authapi import SignupApi, LoginApi

def initialize_routes(api):
    # List users
    api.add_resource(UsersApi, '/api/users') 
    api.add_resource(UserApi, '/api/user/<uid>')
    # Auth
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    
    # Post : adds a Cocop for the User
    api.add_resource(Coopapi,'/api/coop')

    # Get: get the data of a user their Co-ops and roles
    api.add_resource(User_coop_details_api, '/api/ucdetails/<uid>')
    #Post : add User (uid) to Co-op (cid)
    api.add_resource(add_member_api, '/api/member/<uid>/<cid>')
    #api.add_resource()
