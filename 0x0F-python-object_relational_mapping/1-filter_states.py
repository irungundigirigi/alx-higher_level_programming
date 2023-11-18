#!/usr/bin/python3

"""
Lists all states with a name starting with uppercase N
Username, password, and dabase names given as arguments
MySQLdb is an interface for connecting MySQL database server from Python
"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
            print(row)

