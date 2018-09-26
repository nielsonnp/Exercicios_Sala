''' 1. Faça um programa, com uma função que receba três valores,
e que forneça a soma deles.'''

#função

def total (n1, n2, n3):
    soma = (n1 + n2 + n3)
    return soma

#Programa

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o quarto número: '))
n3 = int(input('Digite o terceiro número: '))

print('A soma dos 3 números = {}'.format(total(n1,n2,n3)))