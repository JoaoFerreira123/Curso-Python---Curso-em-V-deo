def aumentar(n, a):
    return n+a


def diminuir(n, d):
    return n-d


def dobro(n,format=False):
    return n*2 if format == False else moeda(n)


def metade(n, format=False):
    return n/2 if format == False else moeda(n)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')