"""
    Comprehension
"""



# Exemplo 1:

nome = 'Fernando Vargas'
print([letra.upper() for letra in nome])  # Um looping dentro de uma lsta para gerá-la

# Exemplo 2:

pessoas = ['gabriel', 'bruno', 'arrascaeta','everton'] 
print([atleta.title() for atleta in pessoas]) # Recebe uma lista e cria uma nova lista com .title

# Exemplo 3:

#Uma lista com um 'for' para gerá-la controlada por um condicional quer verifica se os numeros gerados são par
print(f'São pares {[numero for numero in range(1,10) if not numero % 2]}'
