'''
4- Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.​
'''

import json

pessoa = {
    "nome": "Daniela",
    "idade": 28,
    "cidade": "Curitiba"
}

with open('pessoa.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json, indent=4)

with open('pessoa.json', 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")
