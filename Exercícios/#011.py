#faça um programa que leia a largura e altura de uma parede em m e calcule a área e a quantidade de tinta necessária para pintura
#sabe-se que cada litro de tinta pinta uma área de 2m^2

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
a = larg*alt
tinta = a/2

print('A área da parede é de {} e precisa de {}L de tinta'.format(a, tinta))