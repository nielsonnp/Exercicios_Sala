'''5. Faça um programa que leia 5 números e informe o maior.'''

num = int(input('Digite um número: '))
maior = num

for i in range (1,5):
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
print('O maior número é {}'.format(maior))