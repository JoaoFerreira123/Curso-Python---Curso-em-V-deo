#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
cont = 0
for i in range (n-1, 1, -1):
    if n % i == 0:
        cont += 1
if cont > 0 or n == 1:
    print('O número NÃO é primo')
else:
    print('O número é primo')

