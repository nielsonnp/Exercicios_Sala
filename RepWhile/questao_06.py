'''6. Faça um programa que peça dois números várias vezes, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Escreva uma função para calcular a potência.
pare quando digitar números negativos ou zero'''

def potencia ():
    x = 1
    while True:
        n1 = int(input('Digite a base: '))
        n2 = int(input('Digite o expoente: '))
        p = n1**n2
        print(p)
        x = x + 1
        if n1 <= 0 or n2 <= 0:
            print('Erro: Número digitado menor ou igual a zero')
            break
potencia()



