#crie um programa que leia duas notas e calcule a média, mostrando se foi reprovado ou aprovado
#média abaixo de 5, reprovado
#média entre 5 e 6.9, recuperação
#média acima de 7, aprovado
n1 = float(input('Insira a 1º nota: '))
n2 = float(input('Insira a 2º nota: '))
media = (n1+n2)/2

if media < 5:
    print('A média foi {} e o aluno está\033[31m REPROVADO\033[m'.format(media))
elif media >=5 and media <= 6.9:
    print('A média foi {} e o aluno está\033[33m EM RECUPERAÇÃO\033[m'.format(media))
else:
    print('A média foi {} e o aluno está \033[32mAPROVADO\033[m'.format(media))