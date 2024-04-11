from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'

    serialize_rules= {'-restaurant_pizzas.pizza'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer)
    ingredients = db.Column(db.String(200), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates= 'pizza', cascade='all, delete-orphan')

    # Association proxy to get restaurant for this pizza through restaurant_pizza
    restaurants = association_proxy('restaurant_pizzas', 'restaurant',
                                    creator=lambda restaurant_obj: RestaurantPizza(restaurant=restaurant_obj))

    def __repr__(self):
        return f'<Pizza {self.name}, {self.price}'

    
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    serialize_rules= {'-restaurant_pizzas.restaurant',}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(90), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan' )

    pizzas = association_proxy('restaurant_pizzas', 'pizza',
                                 creator=lambda pizza_obj: RestaurantPizza(pizza=pizza_obj))
    
    def __repr__(self):
        return f'<{self.name} Restaurant>'
    
class RestaurantPizza(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
