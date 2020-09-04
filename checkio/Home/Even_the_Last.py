"""  
    https://py.checkio.org/pt-br/mission/even-last/
"""

def somaDePares(lista):
    soma = 0
    pares = lista[::2]

    for i in pares:
        soma += i

    if len(lista):
        soma *= lista[len(lista) - 1]

    return soma

