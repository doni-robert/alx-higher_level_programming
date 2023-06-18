#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * \
                FROM cities \
                JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    print(", ".join([row[2] for row in query_rows if row[4] == sys.argv[4]]))
    cur.close()
    conn.close()
