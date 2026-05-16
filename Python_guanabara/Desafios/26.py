frase= input('Digite sua frase: ').upper().strip()

print('A letra "a" aparece {} vezes'.format(frase.count('A')))
print('A letra "a" aparece primeiramente na posição {}'.format(frase.find('A')+1))

print('A letra "a" aparece finalmente na posição {}'.format(frase.rfind('A')+1))