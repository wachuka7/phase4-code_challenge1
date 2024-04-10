from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'

    serialize_rules= {'-restaurant.pizza'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer)
    ingredients = db.Column(db.String(200), nullable=False)
    # restaurant_id = db.Column(db.integer, db.ForeignKey('restaurant.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }
    def __repr__(self):
        return f'<Pizza {self.name}, {self.price}'
    
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    serialize_rules= {'-pizza.restaurant',}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(90), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref='restaurants')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [pizza.to_dict() for pizza in self.pizzas]
        }
    
    def __repr__(self):
        return f'<{self.name} Restaurant>'
class RestaurantPizza(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)