#!/usr/bin/python3
"""
module fetching https://alx-intranet.hbtn.io/status
and displaying the r body
"""

import requests
if __name__ == "__main__":

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body r:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
