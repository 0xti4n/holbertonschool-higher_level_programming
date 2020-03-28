#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the database
hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """takes in the name of a state as an argument and
    lists all cities of that state, using the database
    hbtn_0e_4_usa"""

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM cities, states WHERE \
states.name = %s AND cities.state_id = states.id ORDER BY \
cities.id ASC", (argv[4],))
    rows = cur.fetchall()

    to_list = list(map(''.join, rows))
    print(', '.join(to_list))

    cur.close()
    con.close()
