ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break

print(f'{"Nº ":<4}{"Nome: ":<10}{"Média: ":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True: 
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('Finalizou')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')