#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3): #linha
    for j in range(0, 3): #coluna
        m[i][j] = int(input(f'Insira o elemento [{i+1}][{j+1}]: '))

for i in range(0, 3):
    for j in range(0 , 3):
        print(f'[{m[i][j]}] ', end = ' ')
    print() #pra quebrar a linha toda vez que terminar de mostrar cada linha