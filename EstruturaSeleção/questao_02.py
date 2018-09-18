
# 2. Faça um programa que leia dois números e os mostre em ordem crescente.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print('A ordem crescentes dos numeros é {} {}'.format(num2,num1))
elif num2 > num1:
    print('A ordem crescentes dos numeros é {} {}'.format(num1, num2))
else:
    print('Números Iguais')

