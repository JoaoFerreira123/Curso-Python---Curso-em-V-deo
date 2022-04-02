#faca um programa que leia um peso e altura e calcule o IMC, de acordo com:
#abaixo de 18.5, ABAIXO DO PESO
#entre 18.5 e 25, PESO IDEAL
#25 até 30, SOBREPESO
#30 até 40, OBESIDADE
#Acima de 40, OBESIDADE MÓRBIDA
alt = float(input('Informe a sua ALTURA: '))
peso = float(input('Informe o seu PESO: '))
imc = peso/(alt**2)
if imc < 18.5:
    print('O seu IMC é de {:.1f} e você está ABAIXO DO PESO'.format(imc))
elif imc >=18.5 and imc < 25:
    print('O seu IMC é de {:.1f} e você está no PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é de {:.1f} e você está com SOBREPESO'.format(imc))
elif imc >= 30 and imc <= 40: 
    print('O seu IMC é de {:.1f} e você está OBESO'.format(imc))
else:
    print('O seu IMC é de {:.1f} e você está com OBESIDADE MÓRBIDA'.format(imc))
