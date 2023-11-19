#!/usr/bin/python3
"""
This script defines State class - Base class to work with sqlalchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
        State class

        Attr:
            __tablename__ (str): tablename of class
            id(int): Class state id
            name(str): State name of class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
