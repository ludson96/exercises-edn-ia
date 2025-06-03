'''
3- Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP
consultado.
'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200 and "erro" not in resposta.json():
        dados = resposta.json()
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP inválido ou não encontrado.")

cep = input("Digite o CEP (apenas números): ")
consultar_cep(cep)