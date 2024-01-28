#!/usr/bin/python3
"""
script sending  POST request to a given URL with an my_email as a param
and displaying the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    myurl = sys.argv[1]
    my_email = sys.argv[2]

    data = urllib.parse.urlencode({'my_email': my_email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(myurl, data=data) as response:
        print(response.read().decode('utf-8'))
