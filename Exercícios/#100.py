#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 100))

    print(f'Os números sorteados foram: {numeros}')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Na lista {lista}, a soma dos valores PARES é de {soma}')



numeros = []
sorteia(numeros)
somaPar(numeros)
