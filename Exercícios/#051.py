# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Insira o 1º termo da PA: '))
r = int(input('Insira a razão da PA: '))
for i in range (0, 10):
    print('{}'.format(p + r*i), end = ' ') 