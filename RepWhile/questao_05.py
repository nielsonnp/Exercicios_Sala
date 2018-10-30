'''5. Faça um programa que leia vários números. O programa deve parar de solicitar números
ao usuário quando ele digitar um número negativo. Ao final, imprima na tela o maior número
lido.'''

maior = 0

while True:
    n = int(input('Digite um número: '))

    if n > maior:
        maior = n
    elif n < 0:
        break

print('O maior número digitado foi {}'.format(maior))


