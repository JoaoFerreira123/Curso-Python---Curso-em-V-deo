#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
lista = []
dados = []
cont = 0
while True:
    dados.append(input('Digite o nome: '))
    cont += 1
    dados.append(float(input('Digite o peso: ')))
    #verifica quem é o mais leve e mais pesado
    if len(lista) == 0:
        leve = pesado = dados[1]
    else: 
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    lista.append(dados[:]) #copia a lista dados para o índice 1 da lista Lista.
    r = input('Quer Continuar? [S/N] ')
    if r in 'Nn':
        break
    dados.clear()

nomeLeve = []
nomePesado = []

for i in lista:
    if i[1] == pesado:
        nomePesado.append(i[0])
    if i[1] == leve:
        nomeLeve.append(i[0])

print(f'Foram cadastradas {cont} pessoas')
print(f'As pessoas mais leves são {nomeLeve} com {leve} kg')
print(f'As pessoas mais pesadas são {nomePesado} com {pesado} kg')
