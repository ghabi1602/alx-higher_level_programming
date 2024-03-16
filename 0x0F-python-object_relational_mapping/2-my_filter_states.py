#!/usr/bin/python3
""" Displays values in states table that matches the argument """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    cur.execute("""SELECT * FROM states
                WHERE {} LIKE BINARY '{}'""".format(name, sys.argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
