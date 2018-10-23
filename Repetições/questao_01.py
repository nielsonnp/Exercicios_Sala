'''1. Faça um programa para escrever a frase "Eu adoro programar" várias vezes, utilizando um
laço for. A quantidade de vezes que a frase será escrita na tela deve ser fornecida pelo usuário.'''

x = int(input('Quantas vezes você quer repetir o nome? '))

for nome in range (0,x,1):
    print('Eu adoro programar!')
