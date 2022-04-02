#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor =  int(input('Digite o valor a ser sacado: '))
not50 = valor // 50 #divisão inteira
valor %= 50 #valor é o resto da divisão do valor por 50
not20 = valor // 20
valor %= 20
not10 = valor // 10
valor %= 10
not1 = valor // 1

print(f'Notas de 50: {not50}\nNotas de 20: {not20}\nNotas de 10: {not10}\nNotas de 1: {not1}') 
