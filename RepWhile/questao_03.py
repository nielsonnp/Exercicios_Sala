'''3. Faça um programa que, utilizando o laço while, leia 10 números e determine se cada um
deles é par ou ímpar.'''

p = 1 #Inicio do contador

while p <= 10: #Vai contar de 1 até 10
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        print('{} é Par'.format(x))
    else:
        print('{} é Impar'.format(x))
    p = p + 1 #O contador tá incrementando de 1 em 1, quando chegar em 10 para
