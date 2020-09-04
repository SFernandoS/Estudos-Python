""" 
    https://py.checkio.org/en/mission/bigger-price/
"""
from operator import itemgetter

def bigger_price(limit: int, data: list) -> list:
    newList = sorted(data, key = itemgetter('price'))
    newList.reverse()

    return newList[:limit - len(newList)]
