#Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
nome = input('Digite o seu nome: ')
print(nome.upper())
print(nome.lower())

print('Sem espaços, o nome tem {} caracteres'.format(len(nome.replace(' ',''))))
separado = nome.split()
print('O primeiro nome tem {} letras'.format(len(separado[0])))
