''' 3. Faça um programa que pergunte o preço de três produtos e informe qual produto você
 deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

prod1 = float(input('Digite o preço do primeiro produto: '))
prod2 = float(input('Digite o preço do segundo produto: '))
prod3 = float(input('Digite o preço do terceiro produto: '))

if prod1 < prod2 and prod1 < prod3:
    print('É melhor comprar o primeiro produto no valor de {}' .format(prod1))
elif prod2 < prod1 and prod2 < prod3:
    print('É melhor comprar o segundo produto no valor de {}' .format(prod2))
elif prod3 < prod1 and prod3 < prod1:
    print('É melhor comprar o terceiro produto no valor de {}' .format(prod3))
else:
    print('Todos os 3 tem o mesmo valor!')
