'''#Podemos usar o comando import para importar funções de uma determinada biblioteca. 
Um dos exemplos dessa aula é a biblioteca math'''

from math import (sqrt, floor)
num= int(input())
raiz= sqrt(num)
print('A raiz de {} é igual a  {:.2f}'.format(num, floor(raiz)))

#Para baixar outros módulos, acesse o python.org