'''3. Faça um programa que leia 10 números e determine se cada um deles é par ou ímpar.'''

for i in range(11):
    test = int(input('Digite um número: '))
    if test%2 == 0:
        print('{} Par'.format(test))
    else:
        print('{} Ímpar'.format(test))