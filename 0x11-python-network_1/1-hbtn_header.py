#!/usr/bin/python3
""" script that takes in a URL, sends a request
to the URL and displays the value
of the X-Request-Id variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = 'X-Request-Id'
    with urllib.request.urlopen(url) as response:
        the_page = response.getheader(value)
    print(the_page)
