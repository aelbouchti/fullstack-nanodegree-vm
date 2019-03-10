import sys

# Help writting the mapper 
from sqlalchemy import Column, ForeignKey, Integer, String
# Is used in configuration and classe code
from sqlalchemy.ext.declarative import declarative_base
# In order to create our foreignkey relationship
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


### At the end of file ###
engine = create_engine('sqlite://restaurantmenu.db')