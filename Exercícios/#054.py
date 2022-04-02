#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
contMaior = 0
contMenor = 0
for i in range (0, 7):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(i+1)))
    if (date.today().year - ano) < 18:
        contMenor += 1
    elif (date.today().year - ano) >= 18:
        contMaior += 1

print('No grupo de 7 pessoas, {} são maiores de idade e {} são menores de idade'.format(contMaior, contMenor))
