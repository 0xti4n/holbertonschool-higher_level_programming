#!/usr/bin/python3
""" script that takes your Github credentials
(username and password) and uses the Github API
to display your id"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    my_username = argv[1]
    my_token = argv[2]

    try:
        r = requests.get(url, auth=(my_username, my_token))
        data = r.json()
        print(data['id'])
    except KeyError:
        print("None")
