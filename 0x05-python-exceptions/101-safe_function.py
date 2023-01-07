#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        sys.stderr.write("Exception: {}\n".format(err))
    finally:
        return result
