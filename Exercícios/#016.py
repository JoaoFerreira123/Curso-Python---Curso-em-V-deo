#crie um programa que leia um número real e mostre a sua porção inteira (truncar)
from math import trunc

n = float(input('Digite um número real: '))
print(trunc(n))

#outra maneira de fazer isso sem a biblioteca math é:
#print(int(n))