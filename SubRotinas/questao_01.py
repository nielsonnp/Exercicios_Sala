''' 1. Faça um programa, com uma função que receba três valores,
e que forneça a soma deles.'''

#função

def total (n1, n2, n3):
    soma = (n1 + n2 + n3)
    return soma

#Programa

n10 = int(input('Digite o primeiro número: '))
n20 = int(input('Digite o segundo número: '))
n30 = int(input('Digite o terceiro número: '))

print('A soma dos 3 números = {}'.format(total(n10,n20,n30)))