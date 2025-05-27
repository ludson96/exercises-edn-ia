'''
Crie um programa para o professor registrar as notas da turma.

Regras:


Continuar solicitando notas até que o professor digite 'fim'.


Aceitar apenas notas entre 0 e 10.


Ignorar notas inválidas e continuar solicitando.


Ao final, mostrar a média da turma.
'''

notas = []

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite uma nota numérica.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
