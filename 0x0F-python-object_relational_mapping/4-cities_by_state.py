#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    #  MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # SQL querry to fetch all cities-states ordered by cities.id
    querry = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(querry)

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
