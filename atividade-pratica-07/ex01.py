'''
1-  Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 
'''

import re
import statistics

tempos = []

with open('log.txt', 'r') as arquivo:
    for linha in arquivo:
        match = re.search(r'Tempo de execução: ([\d.]+)', linha)
        if match:
            tempos.append(float(match.group(1)))

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    print(f"Média: {media:.2f} segundos")
    print(f"Desvio padrão: {desvio:.2f} segundos")
else:
    print("Nenhum tempo encontrado no log.")
