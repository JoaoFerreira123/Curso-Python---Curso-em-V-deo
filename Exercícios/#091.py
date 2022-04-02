#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado..
import imp
from time import sleep
from random import randint
from operator import itemgetter

print("Valores sorteados: ")
jogo = {"Jogador 1": randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6),
        }
for i, j in jogo.items(): #i pega a chave e j pega o valor
    print(f'{i} tirou {j} no dado')
    sleep(0.5)

print('=-'*20)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #coloca em ordem decrescente em forma de lista
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)

