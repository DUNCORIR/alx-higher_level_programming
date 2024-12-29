#!/usr/bin/python3
"""
Script prints the first State Object from thr database
hbtn_0e_6_usa using SQLAlchemy.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create database engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create configured "Session" class and a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for first State object
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Close the session
    session.close()

    if __name__ == "__main__":
        main()
