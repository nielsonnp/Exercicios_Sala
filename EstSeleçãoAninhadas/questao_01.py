
# 1. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo ou nulo.

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número {} é positivo'.format(numero))
elif numero < 0:
    print('O número {} é Negativo '.format(numero))
else:
    print('O número informado é nulo!')