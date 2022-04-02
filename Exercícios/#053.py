# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite a frase: ').strip().upper().replace(' ', '') #sem espaços com o strip e o replace e tudo em maiusculo
inv = frase[::-1] #fatiamento, fatiando "ao contrário", ou seja, invertendo
if inv == frase:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
