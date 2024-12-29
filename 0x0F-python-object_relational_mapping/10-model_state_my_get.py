#!/usr/bin/python3
"""
Script prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """ Get arguments and query database."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querry for the state
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()


if __name__ == "__main__":
    main()
