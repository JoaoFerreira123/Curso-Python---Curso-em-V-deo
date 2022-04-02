#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = input('Insira o nome do jogador: ')
gol = input('Insira o número de gols: ') #não coloca int pois ele não deixa ficar em branco
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '': #se eu não digitei nada
    ficha(gols=gol) #só passa o parâmetro do gol.
else:
    ficha(nome, gol)
