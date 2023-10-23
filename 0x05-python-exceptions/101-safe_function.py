#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        this_myresult = fct(*args)
        return this_myresult
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
