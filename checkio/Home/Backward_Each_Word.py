""" 
    https://py.checkio.org/en/mission/backward-each-word/
"""

def backward_string_by_word(text: str) -> str:

    lista = [palavra[::-1] for palavra in text.split(' ')]
    lista = ' '.join(lista)

    return lista
