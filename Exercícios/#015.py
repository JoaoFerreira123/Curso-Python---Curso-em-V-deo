#faça um programa que pergunte a quantidade de dias e km rodados de um carro alugado e calcule o valor do aluguel
#considere que o carro custa 60 reais por dia e 15 centavos por km rodado

d = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos KM foram rodados: '))

preco = (60*d)+(0.15*km)

print('O valor do aluguel é R$: {:.2f}'.format(preco))