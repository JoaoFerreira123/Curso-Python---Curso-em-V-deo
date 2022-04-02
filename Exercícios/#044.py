#faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
#a vista/dinheiro/cheque, 10% de DESCONTO
#a vista no cartão, 5% de DESCONTO
#em até 2x no cartão, PREÇO NORMAL
#3x ou mais no cartão, 20% de juros no valor total
valor = float(input('Insira o preço: '))
print('''Insira o método de pagamento
[1] para A VISTA/CHEQUE
[2] PARA A VISTA NO CARTÃO
[3] EM ATÉ 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
metodo = int(input('Método de Pagamento: '))
if metodo ==  1:
    print('10% de desconto, valor total de R$:{}'.format(valor - (0.1*valor)))
elif metodo == 2:
    print('5% de desconto, valor total de R$:{}'.format(valor - (0.05*valor)))
elif metodo == 3:
    print('Sem desconto, valor total de R$:{}'.format(valor))
elif metodo == 4:
    print('20% de juros, valor total de R$:{}'.format(valor + (0.2*valor)))