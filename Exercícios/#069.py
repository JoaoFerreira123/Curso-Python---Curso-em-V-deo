#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 
maior = homem = mulherMenor = 0
resp = 'S'
while resp in 'Ss':
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').upper().strip()[0]
    resp = input('Deseja cadastrar mais alguém? [S/N] ').upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherMenor += 1

print(f'Total de pessoas com mais de 18 anos: {maior}\nAo todo foram cadastrados {homem} homens\nHá {mulherMenor} mulheres com menos de 20 anos')
