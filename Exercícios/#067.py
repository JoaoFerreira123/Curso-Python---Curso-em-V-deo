# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
while True:
    n = int(input('Digite um valor [negativo para parar]: '))
    if n < 0:
        break
    for i in range (0, 11):
        print(f'{n} x {i:2} = {n*i}')
        

