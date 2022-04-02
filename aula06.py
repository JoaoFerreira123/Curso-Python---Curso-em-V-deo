n1 = int(input ('Digite um valor: '))
n2 = int(input ('Digite outro valor: '))
print (type(n1))
soma = (n1+n2)
# print("A soma entre", n1, "e", n2, 'é', soma) fazendo assim funciona, mas é mais primitivo

print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

x = input('Digite Algo: ')
print(x.isalnum())

y = input('Digite Outro Algo: ')
print(y.isupper())