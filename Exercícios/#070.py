#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 
total = barato = contCaro = cont = 0
continuar = 'S'
nomeBarato = ''
while continuar in 'Ss':
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto. R$: '))
    total += preco
    cont+=1
    if preco > 1000:
        contCaro += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomeBarato = nome
    continuar = input('Deseja cadastrar mais algum produto? [S/N] ').upper().strip()[0]

print(f'O total é R$: {total}\nHá {contCaro} produtos acima de R$: 1000\nO produto mais barato é o {nomeBarato} ')

    

