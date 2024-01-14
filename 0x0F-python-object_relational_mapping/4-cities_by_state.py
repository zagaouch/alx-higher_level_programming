#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    query = "SELECT cities.`id`, cities.`name`, states.`name` FROM `cities` \
    AS cities INNER JOIN `states` AS states ON cities.`state_id` = states.`id`\
    ORDER BY cities.`id`;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    con.close()
