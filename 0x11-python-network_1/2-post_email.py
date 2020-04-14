#!/usr/bin/python3
"""script that takes in a URL and an email, sends
a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]
    post_data = urllib.parse.urlencode(data).encode('ascii')
    with urllib.request.urlopen(url, post_data) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))
