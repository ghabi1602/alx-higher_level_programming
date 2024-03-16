#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == __main__:
    db = MySQLdb.connect(host="localhost",
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)

    my_cursor = db.cursor()

    my_cursor.execute("SELECT * FROM states")

    rows = my_cursor.fetchall()

    for row in rows:
        print(row)

    my_cursor.close()
    db.close()
