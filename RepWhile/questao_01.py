'''1. Faça um programa para escrever a frase "Eu adoro programar" várias vezes, utilizando
um laço while. A quantidade de vezes que a frase será escrita na tela deve ser fornecida
pelo usuário.'''


fim = int(input('Quantas vezes você quer repetir o nome? '))
x = 1

while x <= fim:
    print('Eu adoro programar!')
    x = x + 1
