#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
contImpar = contPar = 0
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
        contPar +=1
    else:
        lista[1].append(n)
        contImpar += 1
lista[0].sort()
lista[1].sort()
print(f'Os pares são: {lista[0]} e os ímpares são: {lista[1]}')