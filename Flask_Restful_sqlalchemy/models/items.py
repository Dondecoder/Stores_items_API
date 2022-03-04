from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.FLOAT())

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') # this is like the JOIN statement in SQL which allows you to add two queries. It allows you to create the relationship between
    # ItemModel and StoreModel 

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first() # this essentially is using sqlalchemy to create queries and filer queries where name = name. 
        # this is pretty much doing the same as SELECT * FROM items WHERE name = name LIMIT 1 which means the first one 

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        