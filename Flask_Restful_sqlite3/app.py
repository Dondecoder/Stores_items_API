from flask import Flask, app
from flask_restful import Api # Resource is just a thing our Api can return
# from flask_jwt import JWT, jwt_required

# from security import authenticate, identity
from user import UserRegister
from items import Item, ItemList
app = Flask(__name__) # to create an app
app.secret_key = 'patrik' # < -- this is used to tie a secret key to your api 
api = Api(app) # going to allow us to add resources very easily to it. It works with resources and every resource is a class 

# jwt = JWT(app, authenticate, identity) # this creates /auth endpoint 


# This is a student Resource that was created to help simplify the process of creating a CRUD Api please refer to the readme for more info

# class Student(Resource):

#     def get(self, name):
#         return {'student': name} # simple it's just simply going to return the name of the student


#     def post():
#         pass

#     def put():
#         pass

#     def delete():
#         pass 

# api.add_resource(Student, '/student/<string:name>') # this adds the resource to the the api. This would be needed to save the path 
# # of the student decorator this translates to http://127.0.0.1.5000/student/Rolf 

# app.run(port=5000)

api.add_resource(Item, '/item/<string:name>') # this adds the resource to the the api. This would be needed to save the path 
# of the item decorator this translates to http://127.0.0.1.5000/item/<item name> 
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True) # adding debug = True will allow you to get better error messages if your app has a bug. 