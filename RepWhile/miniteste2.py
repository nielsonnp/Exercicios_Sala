'''Crie um programa para verificar a temperatura de uma cidade ao longo de vários dias. Seu programa deve:

Possuir uma função que receba a temperatura do dia como parâmetro e mostre a mensagem “Temperatura
agradável”, o valor for maior ou igual a 20 e menor a 30. Caso a temperatura fornecida seja menor
que 20, deverá ser exibida a mensagem “Temperatura fria” e se for maior ou igual a 30, a função deve exibir
a mensagem “Temperatura muito quente”; A leitura das temperaturas (e a consequente chamada da função de
verificação das temperaturas) deve ser realizada até que o usuário digite um valor maior do que 50 ou
menor do que -50.

Bonus: Armazene as temperaturas lidas em uma lista. Ao final, exiba a quantidade de temperaturas lidas e a média
das temperaturas neste período.'''

#Função
def temperatura (t2):

    if t2 >= 20 and t2 < 30:
        print('Temperatura agradável')
    elif t2 < 20:
        print('Temperatura fria')
    elif t2 >= 30:
        print('Temperatura muito quente')

#Programa
L=[]
soma = 0
x = 0

while True:
    t = float(input('Digite a temperatura: '))
    if t < -50 or t > 50:
        break
    L.append(t)
    soma += L[x]
    x += 1
    temperatura(t)

print('Quantidade de temperaturas lidas =', len(L))
if len(L) > 0:
    print('Média das temperaturas neste período = {:.2f}'.format(soma/x))