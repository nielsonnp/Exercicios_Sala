'''5. Faça um programa que leia 5 números e informe o maior e menor número.'''

maior = 0
menor = 1000
for i in range (1,6):
    n = int(input('Digite um número: '))
    if n>maior:
        maior = n
    if n < menor:
        menor = n
print('O menor número é {} e o maior número é {}'.format(menor, maior))