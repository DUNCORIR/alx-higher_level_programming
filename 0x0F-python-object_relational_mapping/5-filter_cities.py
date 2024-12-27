#!/usr/bin/python3
"""
Script that takes in state as argument and lists all cities in the state
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    #  MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # State name input from user.
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        user=username,
        host='localhost',
        db=database,
        passwd=password,
        port=3306,
        charset='utf8'
    )

    # Create a cursor object
    cursor = db.cursor()

    # Exe.SQL querry with parameterized query to prevent SQL injection.
    querry = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(querry, (state_name,))

    # Fetch and print results
    rows = cursor.fetchall()
    # Convert each item to string
    cities = [str(row[0]) for row in rows]
    # Print cities as a coma-separated string
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
