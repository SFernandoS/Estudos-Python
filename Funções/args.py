"""
*args

O paramêtro args , colocam os valores extras em uma tupla
"""

#Exemplo

def soma_numeros(*args):
    return f'A soma dos numeros = {sum(args)}'


print(soma_numeros(1, 2, 3, 4, 5, 6))
