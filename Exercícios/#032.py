#faça um programa que leia um ano e mostre se ele é BISSEXTO
from datetime import date
print('Digite um ano. Digite 0 para analisar o ano atual')
ano = int(input('Digite o Ano: '))

if ano == 0:
    ano = date.today().year #se digitar 0, ele pega o ano atual do computador
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0: #é bissexto se for divisivel por 4 E se não for divisível por 100 OU se for divisível por 400
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO É BISSEXTO')

