#escreva um programa que leia dois números inteiros e comapre-os, mostrando na tela uma msg
#O primeiro é maior OU o segundo é maior OU os dois são iguais
n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))

if n1>n2:
    print('O primeiro é maior')
elif n1<n2:
    print('O segundo é maior')
else:
    print('Os números são iguais')