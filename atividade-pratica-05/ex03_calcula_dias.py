'''
3- Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
'''

from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_em_anos = ano_atual - ano_nascimento
    return idade_em_anos * 365
