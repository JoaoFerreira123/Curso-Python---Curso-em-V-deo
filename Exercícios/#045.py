#crie um programa que faça o computador jogar PEDRA, PAPEL E TESOURA (JOKENPÔ)
from time import sleep
from random import randint
comp = randint(1,3)
print('\033[032m PEDRA - PAPEL - TESOURA\033[m')
print('=' * 20)
print('''ESCOLHA A SUA JOGADA
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')
print('=' *20)
player = int(input('Digite a sua opção: '))
print('JO')
sleep(0.5) #digita o tempo em SEGUNDOS que vai ocorrer uma PAUSA
print('KEN')
sleep(0.5)
print('PO')
if comp ==  player:
    print('EMPATE')
elif comp == 1 and player == 2:
    print('Computador Escolheu Pedra então VOCÊ PERDEU')
elif comp == 1 and  player == 3:
    print('Computador Escolheu Pedra então VOCÊ PERDEU')
elif comp == 2 and player == 1:
    print('Computador Escolheu Papel então VOCÊ GANHOU')
elif comp ==  2 and player == 3:
    print('O computador escolheu PAPEL então VOCÊ GANHOU')
elif comp == 3 and player == 1:
    print('O computador escolheu TESOURA então VOCÊ GANHOU')
elif comp == 3 and player == 2:
    print('O computador escolheu TESOURA então VOCÊ PERDEU')


#poderia fazer também com 
#opções = ('Pedra', 'Papel', 'Tesoura')
#comp = randint(0,2)
#dai para mostrar a opção eu faria: print('O computador jogou {}.format(opções[comp])) para mostrar o conteúdo do indice do vetor