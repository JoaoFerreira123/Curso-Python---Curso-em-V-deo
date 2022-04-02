#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compar
#considere U$$ 1.00 = R$3.27

real = float( input('Digite o valor em REAIS: '))
print('Com {} reais é possível comprar {:.2f} dólares.'.format(real, real/3.27))