#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the list_states function
    list_states(username, password, database)
