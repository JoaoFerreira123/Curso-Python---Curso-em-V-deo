#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = list() #cria a lista vazia
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor Adicionado')
    else:
        print('Valor Duplicado')
    r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
num.sort()
print(num)
