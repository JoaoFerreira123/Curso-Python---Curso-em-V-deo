def aumentar(n, a):
    return n+a


def diminuir(n, d):
    return n-d


def dobro(n):
    return n*2


def metade(n):
    return n/2

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')