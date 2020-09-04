"""
     https://py.checkio.org/en/mission/sum-numbers/
"""

def sum_numbers(text):
    soma = 0
    for palavra in text.split():
        if palavra.isnumeric():
            soma += int (palavra)
    return soma



