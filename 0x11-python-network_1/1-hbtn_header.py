#!/usr/bin/python3
"""
Python script takes in a URL sending request to the URL,
and display value of X-Request-Id variable found in header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    myurl = sys.argv[1]
    with urllib.request.urlopen(myurl) as response:
        header = response.info()
        x_request_id = header.get("X-Request-Id")
        print(x_request_id)
