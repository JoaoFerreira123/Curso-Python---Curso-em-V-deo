#escreva um programa para aprovar um emprestimo para comprar uma casa. O programa receberá o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario, ou então o emprestimo será negado

valor = float(input('Digite o valor da casa: '))
parcelas = int(input('Digite o número de parcelas: '))
salario = float(input('Digite o seu salário: '))

p = valor/parcelas

if p > (0.3*salario):
    print('O emprestimo não foi aprovado')
else:
    print('O emprestimo foi aprovado')