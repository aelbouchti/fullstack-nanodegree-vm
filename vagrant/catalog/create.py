from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Which database engine we want to communicate with
engine = create_engine('sqlite:///restaurant.db')
# Bind the engine to the base class
# Makes the connection between the class definition
# and the corresponding tables within the database
Base.metadata.bind = engine
# Establishes a link communication between
# code executions and the created engine
DBSession = sessionmaker(bind=engine)
# Creates an instance of DBSession
session = DBSession()

# Create an instance of Restaurant:
firstRestaurant = Restaurant(name='Pizza Hey')
# Add it to the database
session.add(firstRestaurant)
# commit the action
session.commit()

# Find the table that corresponds to the 'Restaurant'
# class and find all the entries in that table
session.query(Restaurant).all()

# Create a menu item called 'cheese_pizza'
cheese_pizza = MenuItem(name="Cheese Pizza", description="Cheese",
                        course="Entree", price="$8.99",
                        restaurant=firstRestaurant)

# add to DB
session.add(cheese_pizza)
session.commit()
session.query(MenuItem).all()