#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados = dict()
dados['nome'] = input('Nome: ')
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['result'] = 'Aprovado'
elif dados['media'] <= 5:
    dados['result'] = 'Reprovado'
else:
    dados['result'] = 'Em Recuperação'

print('='*20)
print(f'Nome é igual a {dados["nome"]}\nMédia é igual a {dados["media"]}\nO aluno está: {dados["result"]}\n')

#poderia ter feito:
#for k, v in dados.items():
    #print(f' {k} é igual a {v}')
    #já mostraria os índices, sem precisar escrever o texto no print.