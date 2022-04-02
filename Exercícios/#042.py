#refaça o desafio #035 acrescentando o recurso de mostrar que tipo de triangulo será formado
#equilatero, TODOS OS LADOS IGUAIS
#isósceles, DOIS LADOS IGUAIS
#escaleno, TODOS OS LADOS DIFERENTES

r1 = float(input('Digite o valor do lado 1: '))
r2 = float(input('Digite o valor do lado 2: '))
r3 = float(input('Digite o valor do lado 3: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    if r1 == r2 == r3:
        print('As 3 retas PODEM formar um triangulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('As 3 retas PODEM formar um triangulo ESCALENO')
    else:
        print('As 3 retas PODEM formar um triangulo ISÓSCELES')
else:
    print('As 3 retas NÃO PODEM formar um triangulo')