#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Check for correct arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./16-model_state_fetch_all.py",
            "<mysql username> <mysql password> <database name>"
        )
        sys.exit(1)

    # Database connection setup
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and their associated City objects
    states = session.query(State).join(City).order_by(State.id, City.id).all()

    # Print results in the specified format
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close session
    session.close()
