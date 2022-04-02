#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo
#cada uma das 3 retas deve ser menor do que a soma do comprimento dos outros dois

r1 = float(input('Digite o valor do lado 1: '))
r2 = float(input('Digite o valor do lado 2: '))
r3 = float(input('Digite o valor do lado 3: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As 3 retas PODEM formar um triangulo')
else:
    print('As 3 retas NÃO PODEM formar um triangulo')