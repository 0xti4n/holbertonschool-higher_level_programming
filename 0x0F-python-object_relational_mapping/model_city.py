#!/usr/bin/python3
"""python file that contains the class definition
of a City and"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Class City"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False,)
