import sys

# Help writting the mapper 
from sqlalchemy import Column, ForeignKey, Integer, String
# Is used in configuration and classe code
from sqlalchemy.ext.declarative import declarative_base
# In order to create our foreignkey relationship
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__='restaurant'
    name = Column(String(80), nullable=False)
    rest_id = Column(Integer, primary_key=True)

class MenuItem(Base):
    __tablename__='menu_item'
    name = Column(String(80), nullable=False)
    menu_id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.rest_id'))
    restaurant = relationship(Restaurant)
### At the end of file ###
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)