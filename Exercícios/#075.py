#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pare


numeros = tuple(int(input(f'Digite o {i}º valor: ')) for i in range(1, 5))
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')

print(f'Os números pares foram: ', end = '')
for j in numeros:
    if j % 2 == 0:
        print(j, end = ' ')
    