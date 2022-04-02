#faça um programa que leia o comprimento do cateto oposto e do adjacente de um triang. ret., calcule e mostre o comprimento da hipotenusa
from math import sqrt as raiz
o = float(input('Digite o cateto oposto: '))
a = float(input('Digite o cateto adjacente: '))

h = raiz(o**2+a**2)

print('A hipotenusa é: {}'.format(h))

#há também na biblioteca math a função hypot(CO, CA) que calcula a hipotenusa