#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    # Parse Arguments.
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to join State and City
    results = session.query(
        State.name, City.id, City.name
    ).join(City).order_by(City.id).all()

    # Print the results
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")


if __name__ == "__main__":
    main()
