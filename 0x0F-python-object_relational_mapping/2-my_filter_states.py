#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name,
    #  and state name from command line arguments
    username, password, database, SNme = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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

    # Create the SQL qry using format with user input
    qry = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(SNme)

    # Execute the SQL qry
    cursor.execute(qry)

    # Fetch all rows from the result set
    matching_states = cursor.fetchall()

    # Display the results
    for state in matching_states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
