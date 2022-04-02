#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Digite o 1º Termo da PA: '))
r = int(input('Digite a Razão da PA: '))
cont = 0
while cont < 10:
    print('{}'.format(p + r*cont), end = ' ') #essa linha e igual o #051
    cont += 1