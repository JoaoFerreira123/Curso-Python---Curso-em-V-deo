#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
sair = False
while sair != True:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    op = int(input('Digite a sua OPÇÃO: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif op ==2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        sair = True
    else:
        print('Opção Inválida. Tente novamente')


