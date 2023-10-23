#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
    except Exception:
        pass
    finally:
        try:
            print("Inside result: {}".format(value))
        except Exception:
            print("Inside result: {}".format(None))
            return None
    return value
