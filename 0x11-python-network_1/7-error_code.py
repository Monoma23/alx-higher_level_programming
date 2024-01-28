#!/usr/bin/python3
"""
script taking in a URL, sending a request to the URL and displaying
the body of the res. If the HTTP status code is greater than or equal to
400 it prints an error message with the HTTP status code
"""

import requests
import sys

if __name__ == "__main__":
    myurl = sys.argv[1]
    res = requests.get(myurl)

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
