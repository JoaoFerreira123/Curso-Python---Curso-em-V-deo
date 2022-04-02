#faça um programa que leia um salário e calcule o seu aumento
#para salários superiores a 1250, calcule um aumento de 10%
#para salários inferiores ou iguais, o aumento é de 15%
s = float(input('Digite o salário: '))
if s > 1250:
    print('Houve um aumento de 10% e o valor total é de R$: {}'.format((s*0.1)+s))
else:
    print('Houve um aumento de 15% e o valor total é de R$: {}'.format((s*0.15)+s))