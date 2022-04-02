# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
somaIdades = 0
idadeMaior = 0
nomeVelho = ''
contMulher = 0

for i in range(1, 5):
    nome = input('Digite o nome da {}º pessoa: '.format(i))
    idade = int(input('Digite a idade da {}º pessoa: '.format(i)))
    sexo = input('Digite o sexo da {}º pessoa [M / F]: '.format(i)).upper()
    somaIdades = somaIdades + idade
    media = somaIdades/4
    if i == 1 and sexo == 'M':
        idadeMaior = idade
        nomeVelho = nome
    if sexo == 'M' and idade > idadeMaior:
        idadeMaior = idade
        nomeVelho = nome   
    if sexo == 'F' and idade < 20:
        contMulher += 1

print('A média de idade do grupo é de {} anos'.format(media))
print('O nome do homem mais velho é {}'.format(nomeVelho))
print('Há {} mulheres com menos de 20 anos'.format(contMulher))