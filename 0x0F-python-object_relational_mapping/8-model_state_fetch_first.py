#!/usr/bin/python3
"""
Script that prints the first State
object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        return

    # Get the MySQL username, password, and database name from the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine that connects to the MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )
    # Bind the engine to the Base
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if a state is found, and print the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
