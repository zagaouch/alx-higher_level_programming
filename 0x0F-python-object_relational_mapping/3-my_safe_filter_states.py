#!/usr/bin/python3
""" write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections."""

if __name__ == "__main__":

    import MySQLdb
    import sys

    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    con.close()
