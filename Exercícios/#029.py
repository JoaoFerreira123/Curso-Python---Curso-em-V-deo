#escreva um programa que  leia a vel. de um carro. se ultrapassar 80km/h, mostre uma msg dizendo que foi multado
#a multa vai custar R$: 7.00 por cada km acima do limite. mostrar o valor da multa

vel = float(input('Insira a Velocidade: '))

if vel > 80:
    multa = (vel-80)*7
    print('Você foi multado em R$: {}'.format(multa))
else:
    print('Você não foi multado')