#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
dados = dict()
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = 2022 - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0  = não possui): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Digite o salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - 2022

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')