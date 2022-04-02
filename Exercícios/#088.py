#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
jogos = []
lista = []
n = int(input('Quantos jogos quer sortear? '))
total = 1
while total <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: #se não for repetido
            lista.append(num)
            cont+= 1
        if cont >= 6: #só quero 6 números por jogo
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')