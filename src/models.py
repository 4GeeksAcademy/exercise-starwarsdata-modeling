import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    pass

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), primary_key=True)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)
    pass

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    pass

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    pass

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
