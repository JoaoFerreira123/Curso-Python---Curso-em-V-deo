# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

c = ('\033[m',  # sem cores
    '\033[0;30;41m',  # vermelho
    '\033[0;30;42m',  # verde
    '\033[0;30;43m',  # amarelo
    '\033[0;30;44m',  # azul
    '\033[0;30;45m',  # roxo
    '\033[7;30m'  # branco
    )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end = '')
    help(com)
    print(c[0], end='')

def título(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')

#programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)