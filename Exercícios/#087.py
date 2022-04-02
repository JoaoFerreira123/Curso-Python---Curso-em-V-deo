#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaTerceira = 0
for i in range(0, 3): #linha
    for j in range(0, 3): #coluna
        m[i][j] = int(input(f'Insira o elemento [{i+1}][{j+1}]: '))
        if m[i][j] % 2 == 0:
            somaPar = m[i][j] + somaPar
        if j == 2:
            somaTerceira = m[i][j] + somaTerceira

for i in range(0, 3):
    for j in range(0 , 3):
        print(f'[{m[i][j]}] ', end = ' ')
    print() #pra quebrar a linha toda vez que terminar de mostrar cada linha

print('='*20)
print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaTerceira}')
print(f'O maior valor da segunda linha é: {max(m[1])}')
