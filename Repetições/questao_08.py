'''8. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares.'''

pares = 0
impares = 0

for i in range (1,5):
    numeros = int(input('Digite um número: '))

    if numeros % 2 == 0:
        pares = pares + 1
        print('Par')
    else:
        impares = impares + 1
        print('Ímpar')

print('Pares: {} e Ímpares: {}'.format(pares,impares))