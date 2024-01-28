#!/usr/bin/python3
"""
fetching and printing the latest 10 commits from a GitHub repository.
Usage: ./100-github_commits.py repository owner
"""

import requests
import sys

if __name__ == "__main__":
    myurl = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    try:
        r = requests.get(myurl)
        resDict = r.json()
        for k in range(0, 10):
            print("{}: {}".format(resDict[k].get('sha'), resDict[k].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
