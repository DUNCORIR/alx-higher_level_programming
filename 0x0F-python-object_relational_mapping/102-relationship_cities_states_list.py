#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys


def main():
    # Validate command-line arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./script.py <mysql username>",
            "<mysql password> <database name>"
        )
        sys.exit(1)

    # Parse arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create database engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City objects and access State using the relationship
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    main()
