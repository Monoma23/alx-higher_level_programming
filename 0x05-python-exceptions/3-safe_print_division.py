#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_result = a / b
    except (ZeroDivisionError):
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
        return div_result
