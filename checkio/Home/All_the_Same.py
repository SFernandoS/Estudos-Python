""" 
    https://py.checkio.org/en/mission/all-the-same/
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for i in range(len(elements)):
        for j in range(len(elements)):
            if elements[i] != elements[j]:
                return False
    return True
