#!/usr/bin/python3
"""
Script that safely lists all states where
the name matches the user-supplied argument
from the database hbtn_0e_0_usa.
It uses parameterized queries to prevent SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":

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

    # Parameterized query to prevent SQL injection.
    querry = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(querry, (state_name,))

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
