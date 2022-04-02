#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
def area(larg, comp):
    print(f'A área de um terreno de {larg} por {comp} é de {larg*comp}m²') #esse ² é ALT + 253

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
