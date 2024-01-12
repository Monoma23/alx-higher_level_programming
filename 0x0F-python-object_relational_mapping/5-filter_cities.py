#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from command line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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

    # Create the parameterized SQL query to retrieve cities of the specified state
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the SQL query with the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()
