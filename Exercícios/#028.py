#escreva um programa que gere um número aleatório entre 0 e 5 e peça ao usuário para tentar adivinhar qual o número escolhido
#o programa deverá escrever na tela se o usuário acertou ou não
from random import randint

n = randint(0, 5)

num = int(input('Digite um número: '))
if n == num:
    print('Parabéns, você acertou!')
else:
    print('Não acertou!')
