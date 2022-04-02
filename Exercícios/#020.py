#um professor quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle
n1  = input('Digite o nome do primeiro aluno: ')
n2  = input('Digite o nome do segundo aluno: ')
n3  = input('Digite o nome do terceiro aluno: ')
n4  = input('Digite o nome do quarto aluno: ')

nomes = [n1, n2, n3, n4]

shuffle(nomes) #essa função embaralha o conteúdo de um vetor/lista
print('A ordem de apresentação será: {}'.format(nomes))
