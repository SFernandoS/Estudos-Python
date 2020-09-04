"""
    https://py.checkio.org/en/mission/count-digits/
"""

def count_digits(text: str) -> int:
    soma = 0

    for i in text:
        if i.isnumeric():
            soma += 1

    return soma


