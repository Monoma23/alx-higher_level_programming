#!/usr/bin/python3
""" lists all states from the dabse hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL UN, PSWRD, dabse name, and state name from CL args
    UN, PSWRD, dabse, stNm = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=UN,
        passwd=PSWRD,
        db=dabse
    )

    # Create a cursor object to interact with the dabse
    cursor = db.cursor()

    # Create  parameterized SQL query to retrieve cities of the specified state
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the SQL query with the stNm as a parameter
    cursor.execute(query, (stNm,))

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and dabse connection
    cursor.close()
    db.close()
