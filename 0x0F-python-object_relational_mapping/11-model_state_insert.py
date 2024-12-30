#!/usr/bin/python3
"""
Script that adds State object “Louisiana” to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function to add a new state."""
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creates engine and session.
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adds a new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print new state ID
    print(new_state.id)

    # Then close session
    session.close()


if __name__ == "__main__":
    main()
