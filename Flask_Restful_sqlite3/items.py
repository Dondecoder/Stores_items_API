import sqlite3
from flask_restful import Resource, reqparse
import creates_tables

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required= True,
    help = "This field cannot be left blank!")

    # @jwt_required()

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0]}, 'price': row[1]}

    def post(self,name):  
        if self.find_by_name(name):
            return {'message': "An itetm with name '{}' already exist".format(name)}, 400 # if we found an item and it is not equal to None then the return message will
            # populate. You should put a bad request status code if the user is requesting a name that has already been created. 
        data = Item.parser.parse_args() # force = True means that you do not need the content type header in order for it to work. In case your client does not use
        # normal json type. Problem with this is that you don't look at the header so it will process data through json even if it's not correct. 
        # silent = true does not return an error it just returns none. If you have no clue with this means look into postman in the headers section and content type for
        # more info
        item = {'name': name, 'price': data['price']} # data['price'] it is a dictionary and it will be extracting the price key that it has in the dictionary
        try:
            self.insert(item)
        except:
            return {"message": "An error occured inserting the item"}, 500 # 500 is internal server error
        
        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"

        cursor.execute(query,(item['name'], item['price']))
        connection.commit()
        connection.close()
        

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occured inserting this item."}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured updating this item."}, 500
        return updated_item
    
    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()

    # @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'item deleted'}
        

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})
        
        connection.close()

        return {'items': items} # used to get all items in the items variable