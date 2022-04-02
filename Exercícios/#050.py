# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for i in range(1, 7):
    n = int(input('Insira o {}º inteiro par: '.format(i)))
    if n%2 == 0:
        s += n
print(s)
