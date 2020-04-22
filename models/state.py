#!/usr/bin/python3
"""This is the state class"""
from os import environ
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
import models

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
     if environ.get('HBNB_TYPE_STORAGE') == "db":
         __tablename__ = "states"
         name = Column(String(128), nullable=False)
         cities = relationship("City", backref="state",
                               cascade="all, delete, delete-orphan")
     else:
         @property
         def cities(self):
             """
             List cities
             """
             city_query = models.storage.all(City)
             city_list = []
             for c_value in city_query.values():
                 if c_value.state_id == self.id:
                     city_list.append(c_value)
             return c_value
