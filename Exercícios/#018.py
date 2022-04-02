#faça um programa que leia um angulo e mostre o valor do seno, cosseno e tg do angulo

from math import sin, cos, tan, radians
#tem que passar o angulo em radianos
a = float(input('Digite o ângulo: '))

print('O SENO é: {:.2f}, o COSSENO é: {:.2f} e a TANGENTE é: {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))
#o resultado sai em radianos!