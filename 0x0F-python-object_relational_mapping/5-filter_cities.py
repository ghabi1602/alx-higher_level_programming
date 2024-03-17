#!/usr/bin/python3
"""lists all cities of a certain state"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("""SELECT name FROM cities
                INNER JOIN states
                ON cities.state_id=states.id
                WHERE states.name=%s""", (sys.argv[4],))

    rows = cur.fetchall()

    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
