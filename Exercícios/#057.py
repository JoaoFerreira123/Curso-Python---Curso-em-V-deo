#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = input('Insira o seu sexo [M/F]: ').upper().strip()
while s != 'M' and s != 'F': #poderia fazer também while s not in 'MF':
    s = input('Dados Inválidos. Por favor, informe o seu sexo [M/F]: ').upper().strip()

print('Sexo {} registrado com sucesso'.format(s))