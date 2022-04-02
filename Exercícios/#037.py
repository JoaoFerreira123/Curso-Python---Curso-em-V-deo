#escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversã
#1 para binário, 2 para octal, 3 para hexadecimal
n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''') #note as 3 aspas para fazer em várias linhas, mantendo a formatação
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:])) #esse [2:] é pra não aparecer os dois primeiros caracteres - fatiamento de string
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para OCTAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida')