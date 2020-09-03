""" 
    Comprehension de dicionarios funcionam com a mesma ideia das listas
""" 

#Exemplo:

vogaisENumeros = {'a': 1,'e': 2,'i': 3,'o': 4, 'u': 5}
quadrado = {chave: valor**2 for chave, valor in vogaisENumeros.items()}
print(quadrado)

#Exemplo

issoEhUmaLista = ['a', 'e', 'i', 'o', 'u']
issoEhUmDicionario = {issoEhUmaLista[x-1]: x for x in range(1,6)}
print(issoEhUmDicionario)

#Exemplo (com o set também é análogo)
issoEhUmSet = {x for x in range(1,11)}
print(issoEhUmSet)