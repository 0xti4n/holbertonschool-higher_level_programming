#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the body of the response."""
from sys import argv
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {}

    if len(argv) > 1:
        data['q'] = argv[1]
    elif len(argv) < 1:
        data['q'] = ""
    r = requests.post(url, data)
    try:
        jsn = r.json()

        if len(jsn) == 0:
            print("No result")

        elif 'id' in jsn and 'name':
            print("[{}] {}".format(jsn['id'], jsn['name']))
    except ValueError:
        print("Not a valid JSON")
