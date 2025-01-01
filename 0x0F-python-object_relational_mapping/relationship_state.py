#!/usr/bin/python3

"""
Script contains the class definition of a State and
 an instance Base = declarative_base() using SQLAlchemy.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class links the MySQL table 'states'
    """
    __tablename__ = 'states'

    # Define the id column and name column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # State can have many cities, if State is deleted, cities are also deleted
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )