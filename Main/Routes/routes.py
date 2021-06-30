from Main.api.userapi import UserApi, UsersApi
from Main.api.authapi import SignupApi, LoginApi

def initialize_routes(api):
 api.add_resource(UsersApi, '/api/users')
 api.add_resource(UserApi, '/api/user/<uid>')
 api.add_resource(SignupApi, '/api/auth/signup')
 api.add_resource(LoginApi, '/api/auth/login')