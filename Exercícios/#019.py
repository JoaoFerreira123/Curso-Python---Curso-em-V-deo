#um professor quer sortear 1 dos 4 alunos. faça um programa que leia o nome dos alunos e mostrando o nome do sorteado
from random import choice

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

nomes = [a1, a2, a3, a4] #lista/vetor de alunos

escolhido = choice(nomes) #ele escolhe aleatoriamente um índice do vetor e armazena o conteúdo na variável escolhido
#outra opção seria fazer direto print('O escolhido foi: {}'.format(choice([a1, a2, a3, a4])))
print('O aluno escolhido foi: {}'.format(escolhido))
