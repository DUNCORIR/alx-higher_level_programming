#!/usr/bin/python3

"""
Script  lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Base Query states containing 'a'
    query = session.query(State)
    # Filter to select states with 'a' in their name
    filtered_query = query.filter(State.name.like('%a%'))
    # filtered results by State.id in ascending order
    ordered_query = filtered_query.order_by(State.id)
    # Execute the query and fetch all matching records
    states_with_a = ordered_query.all()

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
