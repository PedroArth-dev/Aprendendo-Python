x= float(input('Largura da parede: '))
y= float(input('Altura da parede: '))

z= x*y
t= z/2

print('Sua parede tem {:.1f} m2. Você precisará de {:.1f} litros de tinta'.format(z,t))