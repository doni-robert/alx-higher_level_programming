#!/usr/bin/python3
""" Class definition of a State and an instance Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a class State

    Attributes:
        id(int): id of the state
        name(str): name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
