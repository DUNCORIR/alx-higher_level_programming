#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function to delete states with 'a'"""
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creates engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # To query and delete states with 'a' in name
    query = session.query(State).filter(
        State.name.like('%a%')
    )
    states_to_delete = query.all()
    for state in states_to_delete:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    main()
