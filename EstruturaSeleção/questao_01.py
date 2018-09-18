
# 1. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero >= 0:
    print('O número {} é positivo'.format(numero))
else:
    print('O número {} é Negativo '.format(numero))