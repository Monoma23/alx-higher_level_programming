#!/usr/bin/python3
"""
script taking in a URL, sends a request to URL, and displaying
body of the response 

It manages urllib.error.HTTPError exceptions
prints: Error code: followed by the HTTP status cod
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    myurl = sys.argv[1]

    try:
        with urllib.request.urlopen(myurl) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
