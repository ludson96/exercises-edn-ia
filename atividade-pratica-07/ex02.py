'''
2- Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​
'''

import csv

pessoas = [
    {"Nome": "Ana", "Idade": 30, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 25, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla", "Idade": 35, "Cidade": "Belo Horizonte"}
]

with open('pessoas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    campos = ['Nome', 'Idade', 'Cidade']
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(pessoas)

print("Arquivo CSV criado com sucesso.")
