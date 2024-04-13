from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from . import db

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'

    serialize_rules = {'-restaurant_pizzas.pizza'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer)
    ingredients = db.Column(db.String(200), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')

    # Association proxy to get restaurant for this pizza through restaurant_pizza
    restaurants = association_proxy('restaurant_pizzas', 'restaurant',
                                    creator=lambda restaurant_obj: RestaurantPizza(restaurant=restaurant_obj))

    def __repr__(self):
        return f'<Pizza {self.name}, {self.price}>'