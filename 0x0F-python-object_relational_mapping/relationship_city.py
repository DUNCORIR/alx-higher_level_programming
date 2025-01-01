#!/usr/bin/python3
"""
Script contains the City class for SQLAlchemy ORM.
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base  # Import Base from the updated State model


class City(Base):
    """City class links to the table 'cities' in MySQL."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define the relationship to the State object with the attribute 'state'
    state = relationship("State", back_populates="cities", single_parent=True)
