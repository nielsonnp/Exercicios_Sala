'''6. Faça um programa que leia 5 números e informe a soma e a média dos números.'''

soma = 0

for i in range (1,6):
    n = int(input('Digite um número: '))
    soma = soma+n
print('A soma é = {} e a média é = {} '.format(soma, soma/5))
