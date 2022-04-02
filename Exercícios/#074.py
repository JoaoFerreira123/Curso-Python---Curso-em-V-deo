#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ')
for i in numeros:
    print(i, end = ' ')
print(f'\nO maior dos números é: {max(numeros)} e o menor dos números é: {min(numeros)}')

##para gerar os números, poderia fazer ainda:
#from random import sample
#numeros = tuple(sample(range(10), 5))
#print(numeros)
#print(f'O maior valor é {max(numeros)} e o menor é {min(numeros)}.')

##ou ainda com um for!
#numeros = tuple(randint(1, 10) for i in range(5))
