"""
Definindo funções

def nome_da_função(parametros_de_entrada):
    bloco_da_fução
"""

def calcula_o_quadrado(numero):
    """
        Função que calcula o quadrado de um numero real
        Para ver estar doc: nomeDaFun__doc ou help(nomeDaFunc)
    """
    return f'O quadrado do numero eh: {numero*numero}'

print(calcula_o_quadrado(numero = (float)(input("Digite um numero:"))))