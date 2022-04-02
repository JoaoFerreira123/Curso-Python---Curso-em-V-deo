#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
vitorias = 0
while True:
    jog = int(input('Digite um número: '))
    pi = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    comp = randint(0, 10)
    if (jog + comp) % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(f'Você jogou {jog} e o computador jogou {comp}. Total de {comp + jog} deu {result}')
    if result == 'PAR' and pi == 'P':
        print('Você Venceu! ', end = '')
        print('Vamos Jogar Novamente....')
        vitorias += 1
    elif result == 'ÍMPAR' and pi == 'I':
        print('Você Venceu! ', end = '')
        print('Vamos Jogar Novamente....')
        vitorias += 1
    else:
        print(f'Você perdeu com {vitorias} consecutivas.')
        break
    
