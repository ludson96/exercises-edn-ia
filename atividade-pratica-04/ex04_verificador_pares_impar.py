'''
Crie um programa que solicite números inteiros ao usuário.

Regras:


Continuar pedindo números até que o usuário digite 'fim'.


Informar se o número é par ou ímpar.


Se não for um número inteiro, informar o erro e continuar.


Ao final, mostrar a quantidade total de números pares e ímpares inseridos.
'''

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Número par.")
            pares += 1
        else:
            print("Número ímpar.")
            impares += 1
    except ValueError:
        print("Erro: insira um número inteiro.")

print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
