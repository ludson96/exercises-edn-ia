'''
4-- Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). Ousuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.
'''

import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json().get(f"{moeda}BRL")
        if dados:
            print(f"Moeda: {dados['name']}")
            print(f"Valor atual: R$ {dados['bid']}")
            print(f"Valor mínimo: R$ {dados['low']}")
            print(f"Valor máximo: R$ {dados['high']}")
            print(f"Data/Hora: {dados['create_date']}")
        else:
            print("Código de moeda inválido.")
    else:
        print("Erro ao acessar a API.")

codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo_moeda)
