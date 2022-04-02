#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range (1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(i)))
    if i == 1: #o primeiro peso digitado 
        maior = peso
        menor = peso
    else: #se não for o primeiro, ele vai verificar o resto
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é: {} kg'.format(maior))
print('O menor peso é: {} kg'.format(menor))

#OUTRA POSSÍVEL SOLUÇÃO:
#lst=[]  #lista vazia
#for c in range(1, 6):
#    peso=float(input('Peso da {}ª pessoa: '.format(c)))
#    lst+=[peso]   #adiciona os valores de peso na lista
#print('O Maior peso foi:', max(lst))  #maximo valor da lista
#print('O Menor peso foi:', min(lst))  #minimo valor da lista