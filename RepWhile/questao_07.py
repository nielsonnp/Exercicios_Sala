'''7. Faça um programa que leia vários números e determine se cada um deles é par ou ímpar
O programa deve encerrar se o usuário digitar o valor 0. Adicionalmente, faça a verificação
 do número em uma função, chamada ehPar(valor) que retorna um valor booleano
 (True, se o valor for par; False, se o valor for ímpar).'''


def ehPar ():
    x = 1
    while True: #Ou (x < 10) por exemplo pra pedir 9 números
        n1 = int(input('Digite um número: '))
        if n1 == 0:
            break
        elif n1 % 2 == 0:
            print(True)
        else:
            print(False)
        x = x+1

ehPar()
