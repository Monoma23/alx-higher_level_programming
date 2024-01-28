#!/usr/bin/python3
"""
This script is fetching the URL "https://alx-intranet.hbtn.io/status"
and displaying the body response
"""

import urllib.request

if __name__ == "__main__":
    my_url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(my_url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
