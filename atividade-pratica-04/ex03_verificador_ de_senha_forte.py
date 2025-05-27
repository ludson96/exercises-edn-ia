'''
Crie um programa que verifique se a senha é forte.

Regras:


Senha forte: pelo menos 8 caracteres e pelo menos um número.


Continuar pedindo senha até que uma válida seja inserida ou o usuário digite 'sair'.
'''
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrado.")
        break

    if len(senha) >= 8 and any(c.isdigit() for c in senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Deve conter pelo menos 8 caracteres e 1 número.")
