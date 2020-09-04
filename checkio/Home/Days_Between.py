""" 
    https://py.checkio.org/en/days-diff/
"""

from datetime import date


def days_diff(a, b):
    diferença = date(a[0], a[1], a[2]) - date(b[0], b[1], b[2])

    return abs(diferença.days)
