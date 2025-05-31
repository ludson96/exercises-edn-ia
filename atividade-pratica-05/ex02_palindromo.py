'''
2- : Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).​
​

Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”
'''

import re

def eh_palindromo(texto: str) -> str:
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
