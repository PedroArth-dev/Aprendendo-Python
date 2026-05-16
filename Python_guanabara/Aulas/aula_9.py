#Manipulação de texto (string)

frase='O original nunca se desoriginaliza'

#Fatiamento

print(frase[9])
print(frase[4:10])
print(frase[10:25:2])
print(frase[:4])
print(frase[15:])
print(frase[5::4])

#comprimento

print(len(frase))

#contagem de caracter
print(frase.count('o'))
print(frase.count('o',2,16))

#encontrar texto

a= frase.find('original')
print(a)

print('nunca' in frase)
print('Pneu' in frase)

#Transformação

print(frase.replace('Pneu','sabao'))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())

#pode ser usado para páginas de login por exemplo
print(frase.title())

#Para eliminar espaços inúteis
print(frase.strip())
#para eliminar apenas os espaços finais
print(frase.rstrip())
#eliminar espaços do início
print(frase.lstrip())

#Divisão

print(frase.split())

#junção
print('-'.join(frase))