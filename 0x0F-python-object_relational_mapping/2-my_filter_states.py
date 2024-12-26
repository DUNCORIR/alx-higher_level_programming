#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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

    # Execute the SQL querry
    querry_parts = [
        "SELECT * FROM states WHERE name = ",
        "'{}'".format(state_name),
        " ORDER BY id ASC"
    ]

    querry = "".join(querry_parts)
    cursor.execute(querry)

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
