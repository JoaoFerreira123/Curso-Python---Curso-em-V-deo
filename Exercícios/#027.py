#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite o seu nome: ').strip().split()
print('{}, {}'.format(nome[len(nome)-1], nome[0]))