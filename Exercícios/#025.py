#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome: ').upper().strip()
print('SILVA' in nome)

#ainda tem um problema. Se o nome fosse Silvanete daria True, pois há silva.
#Para resolver esse problema teria que dar um split também 