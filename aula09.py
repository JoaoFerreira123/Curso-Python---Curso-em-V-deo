frase = 'Curso de Python'
print(frase.upper().count('O')) #coloca todas em maiusculo e daí conta quantas O tem

print(frase) #note que não está em maiúsculo. Isso pq ali acima eu só mandei imprimir, eu não "salvei" 
#para REALMENTE trocar tudo para maiúsuclo, teria que fazer frase = frase.upper()

print('Curso' in frase) #vai imprimir True pois 'Curso' existe na string frase

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][0]) #primeira letra 