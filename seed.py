from app import app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza
from models import db

with app.app_context():

    # Delete all rows in tables
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    db.session.commit()
    

    # Add pizza
    p1 = Pizza(name="Roman", price = 20, ingredients= "chicken")
    p2 = Pizza(name="Cuban", price= 28, ingredients= "beef")
    p3 = Pizza(name="Sicilian", price = 27, ingredients= "chicken BBQ")
    p4 = Pizza(name="New York-style", price= 27, ingredients= "chicken Peri Peri")
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

    # Add restaurant
    r1 = Restaurant(name="Home",                 
                 address="Times Tower")
    r2 = Restaurant(name="The Peach",                 
                 address="Huru Tower")
    db.session.add_all([r1, r2])
    db.session.commit()

    # Many-to-many relationship between pizzas and restaurants

    # # Add restaurants to a pizza
    # p1.restaurants.append(r1)
    # p1.restaurants.append(r2)
    # # Add pizzas to a restaurant
    # r2.pizzas.append(p2)
    # r2.pizzas.append(p3)
    # r2.pizzas.append(p4)

    # Many-to-many relationship between pizza and restaurant through restaurant_pizza

    rp1 = RestaurantPizza(price= 15,                    
                    restaurant_id=r1.id,
                    pizza_id=p1.id)
    
    rp2 = RestaurantPizza(price = 10,                    
                    restaurant_id=r2.id,
                    pizza_id=p2.id)
    
    rp3 = RestaurantPizza(price =11,
                        restaurant_id=r1.id,
                        pizza_id=p2.id)
                    

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
