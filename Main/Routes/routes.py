from Main.api.coopapi import Coopapi 
from Main.api.add_member_api import add_member_api 
from Main.api.user_coop_deatils_api import User_coop_details_api, Users_in_coop_api
from Main.api.userapi import UserApi, UsersApi
from Main.api.authapi import SignupApi, LoginApi
from Main.api.productapi import Productapi,Productapi_price,Productapi_quantity, ListAllProduct_api
from Main.api.product_coop_details_api import Productapi_productid, Productapi_Coopid
from Main.api.purchase_history import Purchase_history
from Main.api.expenses_api import Expenses_api
from Main.api.Profit_level_api import Profit_level
from Main.api.price_forecast import PriceAPI


def initialize_routes(api):
    # List users
    api.add_resource(UsersApi, '/api/users') 
    api.add_resource(UserApi, '/api/user/<username>')
    # Auth
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    
    # Post : adds a Cocop for the User
    api.add_resource(Coopapi,'/api/coop')

    # Get: get the data of a user their Co-ops and roles
    api.add_resource(User_coop_details_api, '/api/ucdetails/<username>')
    # Get: User in a Co-op
    api.add_resource(Users_in_coop_api,'/api/coop/users/<cid>')

    #Post : add User (uid) to Co-op (cid)
    api.add_resource(add_member_api, '/api/member/<username>/<cid>')


    #Get: get list of Products created by auth user
    api.add_resource(Productapi, '/api/products')
    
     #Get: get list of Products from all coops (for inventory purposes)
    api.add_resource(ListAllProduct_api, '/api/all_products', '/api/all_products/<id>')


    #Get: get list of Products created by Co-op
    #Post: adds product to Co-op (coopid)
    api.add_resource(Productapi_Coopid, '/api/products/<coopid>')
    

    #Put: update price of product (productId)
    api.add_resource(Productapi_price, '/api/product_price/<productId>/<price>')

    #Put: update quantity of product (productId)
    api.add_resource(Productapi_quantity, '/api/product_quantity/<productId>/<quantity>')
    
    #delete : delete product
    #Get : Get product detals based on name 
    api.add_resource(Productapi_productid, '/api/product_remove/<productid>/<coopid>')

    # Get: get purchase history of coops
    # Post: Add purchase history
    api.add_resource(Purchase_history, '/api/history/<coopid>')
    
    #Get: get Expenses of a coop 
    #Post: Add Expense to a coop 
    api.add_resource(Expenses_api, '/api/expenses/<coopid>')
    
    #Get: get Profit history of a coop 
    #Post: add profit for a coop 
    api.add_resource(Profit_level, '/api/profit/<coopid>')
    #Post : 
    #body : {"input_data": [{"fields": ["date","main_commercial_species","size"],"values": [["2021-01-01","Rey",5]]}]}
    api.add_resource(PriceAPI, '/api/forecast/price')
