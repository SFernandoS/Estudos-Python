""" 
    Listas aninhadas (Nested lists)

    São listas com mais de uma dimensão
"""

#Exemplo:

bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Uma lista de listas, uma matriz 3x3

#Exemplo de como acessar:

[print(listas) for listas in bidimensional]
# Aqui eu acesso cada lista dentro da lista bidimensional

[[print(valor) for valor in listas] for listas in bidimensional] 
# Aqui eu acesso os valores das listas que estão dentro da lista bidimensional