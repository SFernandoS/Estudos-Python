""" 
    https://py.checkio.org/pt-br/mission/three-words/
"""

def checkio(words: str) -> bool:
    words = words.split()
    contaTextos = 0

    for i in words:
        if not i.isnumeric():
            contaTextos += 1
        else:
            contaTextos = 0

        if contaTextos == 3:
            return True

    return False
