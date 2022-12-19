#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        rs = fct(*args)

    except Exception as e:
        sys.stderr.write('Exception: {}\n'.format(e))
        rs = None

    return (rs)
