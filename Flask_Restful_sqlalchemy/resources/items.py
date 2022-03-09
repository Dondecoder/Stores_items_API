from flask_restful import Resource, reqparse
from models.items import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required= True,
    help = "This field cannot be left blank!")

    parser.add_argument('store_id',
    type = int,
    required= True,
    help = "Every item needs a store id.")


    # @jwt_required()

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
    def post(self,name):  
        if ItemModel.find_by_name(name):
            return {'message': "An itetm with name '{}' already exist".format(name)}, 400 # if we found an item and it is not equal to None then the return message will
            # populate. You should put a bad request status code if the user is requesting a name that has already been created. 
        data = Item.parser.parse_args() # force = True means that you do not need the content type header in order for it to work. In case your client does not use
        # normal json type. Problem with this is that you don't look at the header so it will process data through json even if it's not correct. 
        # silent = true does not return an error it just returns none. If you have no clue with this means look into postman in the headers section and content type for
        # more info
        item = ItemModel(name, **data) # data['price'] it is a dictionary and it will be extracting the price key that it has in the dictionary
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item"}, 500 # 500 is internal server error
        
        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
               
        else:
           item.price = data['price']

        item.save_to_db()
        
        return item.json()
   
    # @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}
        

class ItemList(Resource):
    def get(self):
       return {'items': [x.json() for x in ItemModel.find_all()]} # used to get all items in the items variable
    # return {'items': [item.json() for item in ItemModel.query.all()]} alternative to using lambda to retrieve all items. 