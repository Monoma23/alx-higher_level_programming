#!/usr/bin/python3
"""
Sending< POST request to a URL with an email
as a param and displaying the response body
"""

if __name__ == "__main__":
    import sys
    import requests

    rr = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(rr.text)
