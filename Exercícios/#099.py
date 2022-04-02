#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*v):
    maior = v[0]
    for i in v:
        if i >= maior:
            maior = i
    print(f'O maior valor é {maior}')


maior(2, 9, 4, 5, 7, 1)