#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    r = requests.get(url)
    data = r.json()

    for i in range(0, 10):
        print(data[i]['sha'] + " " + data[i]['commit']['author']['name'])
