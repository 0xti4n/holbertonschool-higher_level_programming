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
    i = 0
    length = len(to_list)
    flag = 0
    for i in range(0, length):
        if i == length - 1:
            print("{}".format(to_list[i]), end="")
            flag = 1
        else:
            print("{},".format(to_list[i]), end=" ")
            flag = 1
    if flag == 1:
        print()
    cur.close()
    con.close()
