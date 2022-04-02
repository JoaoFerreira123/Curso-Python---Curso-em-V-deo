#crie um programa que leia um valor em metros e coverta para centimetros e milimetros
x = int (input('Digite o valor em metros: '))
print('{} centímetros\n{} milímetros'.format(x*100, x*1000))