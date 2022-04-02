#faça um programa que leia o preço deum produto e mostre seu novo preço com 5% de desconto
p = float(input('Digite o preço: '))
print('O preço com 5% de desconto é: {:.2f}'.format(p-(p*0.05)))