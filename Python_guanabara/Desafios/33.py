'''n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
n3= int(input('Digite o terceiro número: '))

if n1>n2>n3:
    print('{} É o maior e {} É o menor'.format(n1,n3))
else:
    if n2>n1>n3:
        print('{} É o maior e {} É o menor'.format(n2,n3))
    else:
        if n3>n1>n2:
            print('{} É o maior e {} É o menor'.format(n3,n2))
        else:
            if n1>n3>n2:
                print('{} É o maior e {} É o menor'.format(n1,n2))
            else:
                if n2>n3>n1:
                    print('{} É o maior e {} É o menor'.format(n2,n1))
                else:
                    print('{} É o maior e {} É o menor'.format(n3,n1))'''
#ou
a= int(input('Digite o primeiro número: '))
b= int(input('Digite o segundo número: '))
c= int(input('Digite o terceiro número: '))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))