num= int(input('Digite um número: '))
num2= int(input('Digite um segundo número: '))
s= num+num2
print('A soma entre {} e {} vale {}'.format(num, num2, s))

'''
Se digitamos
int o parentese converte-se em inteiro

float, em um número decimal

bool, em um valor booleano

str, em uma string (cadeia de caracteres)
'''
print(s.is_integer)