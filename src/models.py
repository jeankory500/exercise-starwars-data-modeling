import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(50), unique=True)
    email= Column(String(50))
    name = Column(String(250), nullable=False)
    #userfav = Column(Integer, ForeignKey('favorites.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column (Integer, primary_key=True)
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    charactersfav = Column(Integer, ForeignKey('characters.id'))
    planetsfav = Column(Integer, ForeignKey('planets.id'))
    userfav = Column(Integer, ForeignKey('user.id'))

    
    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    terrian = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    Race = Column(String(255), nullable=False)
    Eye_color = Column(String(255), nullable=False)

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
