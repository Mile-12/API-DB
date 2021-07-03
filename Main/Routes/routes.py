from Main.api.coopapi import Coopapi 
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

    # Get: get the data of users their Co-ops and roles
    api.add_resource(User_coop_details_api, '/api/ucdetails/<uid>')
    #api.add_resource()
