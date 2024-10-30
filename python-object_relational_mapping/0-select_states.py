#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute the query to select all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them in the desired format
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
