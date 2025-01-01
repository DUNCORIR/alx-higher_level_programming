#!/usr/bin/python3

"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_and_city():
    # Check number of arguments passed
    if len(sys.argv) < 4:
        print("Usage: ./100-relationship_states_cities.py", end="")
        print("<mysql username>", end=" ")
        print("<mysql password>", end=" ")
        print("<database>")
        return

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection to MySQL using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State ("California") and a City ("San Francisco")
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the new State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit thescript that creates the State “California”
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    create_state_and_city()