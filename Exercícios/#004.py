#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

x = input("Digite algo: ")

print(type(x))

print('É numérico? {}'.format(x.isnumeric()))
print('É decimal? {}'.format(x.isdecimal()))
print('É alfabético? {}'.format(x.isalpha()))
print('É da tabela ASCII? {}'.format(x.isascii()))
print('É tudo maiúsculo? {}'.format(x.isupper()))
print('É tudo minúsculo? {}'.format(x.islower()))
print('Só possui espaços? {}'.format(x.isspace())) #se só possuir espaço
print('Começa com letra maiúscula? {}'.format(x.istitle())) #se começar com maiúscula 
