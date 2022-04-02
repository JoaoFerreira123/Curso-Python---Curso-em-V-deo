#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite a frase: ').upper().strip()
print('Na frase, tem {} letras A'.format(frase.count('A')))
print('Que aparece primeiro na posição {} e por ultimo na posição {}'.format(frase.find('A')+1, frase.rfind('A')+1))