# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint
print('Acabei de pensar num número de 0 a 10... Tente adivinhar')
n = int(input('Qual é o seu palpite: '))
a = randint(0, 10)
cont = 0
while n != a:
    if n > a:
        print('Menos.. Tente mais uma vez!')
    if n < a:
        print('Mais.. Tente mais uma vez!')
    n = int(input('Qual é o seu palpite: '))
    cont += 1
if n == a:
    print('Vocé acertou com {} tentativas'.format(cont+1)) #tem esse +1 pois o primeiro palpite está fora do while

##outra alternativa é colocar o input SOMENTE dentro do while, daí usaria um flag
#acertou = false
#while not acertou:
#   n = int(input('Qual é o seu palpite: '))
#   cont += 1
#if n == a:
#   acertou = true
#else:
#   if n < a ... E A PARTIR DAI É TUDO IGUAL