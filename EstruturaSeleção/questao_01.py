
# 1. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um número: '))

if (numero % 2) == 0:
    print('O número {} é par '.format(numero))
else:
    print('O número {} é impar '.format(numero))