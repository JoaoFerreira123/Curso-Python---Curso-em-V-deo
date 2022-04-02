#crie um programa que leia o ano de nascimento e informe a categoria do atleta de acordo com a idade
#até 9 anos, MIRIM
#até 14 anos, INFANTIL
#até 19 anos, JUNIOR
#até 20 anos, SENIOR
#acima, MASTER
nasc = int(input('Insira o ano de nascimento: '))
idade = 2022 - nasc
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 20:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')