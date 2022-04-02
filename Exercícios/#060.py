#Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um número para cálculo do FATORIAL: '))
cont = n
fat = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='') #isso pra mostrar o = no final do ultimo valor (que é 1)
    fat = fat * cont
    cont = cont - 1
print(fat)

#outra opção seria:
#from math import factorial
#n = int(input('Digite o número: '))
#f = factorial(n)
#print(f)