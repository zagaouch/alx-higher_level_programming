#!/usr/bin/python3
""" Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows[:-1]:
        print(f"{row[1]}, ", end="")
    if rows:
        print(rows[-1][1])
    else:
        print()
    con.close()
