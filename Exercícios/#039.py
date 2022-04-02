#faça um programa que leia o ano de nascimento de uma pessoa e informe: 
#se ele AINDA vai se alistar no serviço militar, se JÁ É A HORA de se alistar ou se JÁ PASSOU DO TEMPO do alistamento.
#o programa também deve mostrar o tempo que falta ou passou do prazo
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
alist = (date.today().year-ano)
if alist == 18:
    print('Já está na hora de se alistar')
elif alist < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-alist))
else:
    print('Já passou {} anos do prazo de alistamento'.format(alist-18))
