#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = input('Quer Continuar? [S/N]: ')
    if r in 'Nn':
        break
print(f'A lista completa é {par+impar}')
print(f'Os pares são: {par}')
print(f'Os ímpares são: {impar}')
