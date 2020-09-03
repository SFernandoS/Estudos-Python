"""
**kwargs

São 'dicionários' de *args
""" 

#Exemplo:

def minha_funcao(nome, idade, *args, solteiro = False, **kwargs):
    """
        Parâmetros obrigatórios: nome; idade.
        *args: não obrigatório.
        Defalt: solteiro.
        **kwargs: não obrigatório.
    """
    print(f'Nome :{nome}')
    print(f'idade:{idade} anos')
    print("Solteiro" if solteiro else "Casado")
    for argInformacao in args:
        print(f'informacao: {argInformacao}')
    for chaves, valores in kwargs.items():
        print(f'{chaves} : {valores}')


minha_funcao('Fernando', 20,'Estagio','Quinto semestre', solteiro = True, email = 'nandovargas7@gmail.com')




