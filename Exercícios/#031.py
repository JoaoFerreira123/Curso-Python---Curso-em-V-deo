#faça um programa que pergunte a distancia de uma viagem em km e calcule o preço da passagem
#Cobre R$: 0.50 por km para viagens até 200km e R$: 0.45 por km para viagens mais longas

dist = float(input('Digite a distância em KM: '))

if dist <= 200:
    print('O valor da passagem é R$: {}'.format(dist*0.5))
else:
    print('O valor da passagem é R$: {}'.format(dist*0.45))