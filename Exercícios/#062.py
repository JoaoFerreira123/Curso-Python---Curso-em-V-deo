#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
p = int(input('Digite o 1º Termo da PA: '))
r = int(input('Digite a Razão da PA: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print('{}'.format(p + r*cont), end = ' ') #essa linha e igual o #051
        cont += 1

    mais = int(input('\nQuantos termos você quer mostrar a mais: '))
print('Progressão finalizadacom {} termos mostrados'.format(total))
