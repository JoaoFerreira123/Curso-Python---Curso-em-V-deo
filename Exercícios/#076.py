# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9 )
print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)
for i in range(0, 18, 2):
    print(f'{produtos[i]:.<40} R$: {produtos[i+1]:.2f}\n') #aquele :.<40 é pra colocar 40 caracteres preenchidos com . e alinhados a esquerda
print('='*50)