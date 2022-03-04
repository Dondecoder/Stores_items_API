from flask import Flask, app, request
from flask_restful import Resource, Api, reqparse # Resource is just a thing our Api can return
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__) # to create an app
app.secret_key = 'patrik' # < -- this is used to tie a secret key to your api 
api = Api(app) # going to allow us to add resources very easily to it. It works with resources and every resource is a class 

jwt = JWT(app, authenticate, identity) # this creates /auth endpoint 


items = []
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



class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required= True,
    help = "This field cannot be left blank!")

    @jwt_required()

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) # the filter function filters list of items looking for paramater set in filter function
        # write a lamba functon of what you want to filter by. Lamda argument takes two paramaters the item we are filtering and the iterable which means the items
        # list. filter function doesn't return an item or a list it returns a filter an object you can use a list object with the filter function to return a list. 
        # for example list(filter(lambda x: x['name'] == name, items)). Instead of list you can use next which returns the first item found in the filter function. Next
        # can raise an error if there are no items left so we can but None which means if the next function does not find a value it will return none 
        return{'item': item}, 200 if item else 404 # < -- this returns item and if there is an item it returns status code 200(Status ok) 
        # else it returns status code 404(Not found)
        

    def post(self,name):  
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An itetm with name '{}' already exist".format(name)}, 400 # if we found an item and it is not equal to None then the return message will
            # populate. You should put a bad request status code if the user is requesting a name that has already been created. 
        data = Item.parser.parse_args() # force = True means that you do not need the content type header in order for it to work. In case your client does not use
        # normal json type. Problem with this is that you don't look at the header so it will process data through json even if it's not correct. 
        # silent = true does not return an error it just returns none. If you have no clue with this means look into postman in the headers section and content type for
        # more info
        item = {'name': name, 'price': data['price']} # data['price'] it is a dictionary and it will be extracting the price key that it has in the dictionary
        items.append(item)
        return items, 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
        
    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}
        

class ItemList(Resource):
    def get(self):
        return {'items': items} # used to get all items in the items variable

api.add_resource(Item, '/item/<string:name>') # this adds the resource to the the api. This would be needed to save the path 
# of the item decorator this translates to http://127.0.0.1.5000/item/<item name> 
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True) # adding debug = True will allow you to get better error messages if your app has a bug. 