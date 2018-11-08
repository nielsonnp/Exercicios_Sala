'''7. Faça um programa que leia vários números e determine se cada um deles é par ou ímpar
O programa deve encerrar se o usuário digitar o valor 0. Adicionalmente, faça a verificação
 do número em uma função, chamada ehPar(valor) que retorna um valor booleano
 (True, se o valor for par; False, se o valor for ímpar).'''

def ehPar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

x = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    x = x + 1
    print(ehPar(n))

