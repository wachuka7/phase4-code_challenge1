from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from . import db

class RestaurantPizza(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    __table_args__ = (
        db.CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
