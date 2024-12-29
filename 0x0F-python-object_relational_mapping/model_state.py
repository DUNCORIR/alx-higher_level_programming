#!/usr/bin/python3

"""
Script contains the class definition of a State and
 an instance Base = declarative_base() using SQLAlchemy.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class links the MySQL table 'states'
    """
    __tablename__ = 'states'

    # Define the id column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Define the name column
    name = Column(String(128), nullable=False)
