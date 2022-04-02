#nome = input('Qual o seu nome:  ')
#print('Prazer em te conhecer {:*^20}!'.format(nome))


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

soma = n1+n2
mult = n1*n2
div = n1/n2
divInt = n1//n2
exp = n1**n2
resto = n1%n2

print('A soma é: {}, a multiplicação é: {},  a divisão é: {:.3f}'.format(soma, mult, div), end=' ')
print('A divisão inteira é: {}, o exponencial é: {} e o resto é: {}'.format(divInt, exp, resto))