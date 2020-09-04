""" 
    https://py.checkio.org/en/mission/bigger-price/
"""
from operator import itemgetter

def bigger_price(limit: int, data: list) -> list:
    newList = sorted(data, key = itemgetter('price'))
    newList.reverse()

    return newList[:limit - len(newList)]


print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))