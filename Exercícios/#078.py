#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
num = []
posMaior = []
posMenor = [] 
for i in range(0, 5):
    num.append(int(input(f'Digite o {i}º valor: ')))

print(f'Você digitou os valores {num}')

for i, j in enumerate(num): #ele vai percorrer e enumerar. Percorrer com j (valor) e enumerar com i (posição)
    if j == max(num):
        posMaior.append(i)
    if j == min(num):
        posMenor.append(i)

print(f'O maior valor foi {max(num)} na posição {posMaior} e o menor valor foi {min(num)} na posição {posMenor}')
