#faça  um programa que leia três numeros e mostre qual é o maior e qual é o menor
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
maior = n1

if n2 > n1:
    maior = n2

if n3 > n2:
    maior = n3

print('O maior número é: {}'.format(maior))