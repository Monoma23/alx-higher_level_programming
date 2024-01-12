#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line args
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()
