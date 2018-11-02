'''06. Crie uma função que receba a temperatura de uma cidade como parâmetro e mostre a
mensagem “Temperatura agradável”, se for fornecido (pelo usuário) um valor maior ou igual
a 20 e menor ou igual a 30. Caso a temperatura fornecida seja menor que 20, deverá
ser exibida a mensagem “Temperatura fria” e se for maior que 30, a função deve exibir a
mensagem “Temperatura muito quente”.

#Função
def temperatura (t1):

    if t1 > 30:
        print('Temperatura muito quente')
    elif t1 < 20:
        print('Temperatura fria')
    else:
        print('Temperatura agradável')

#Programa
t2 = int(input('Digite a temperatura: '))

temperatura(t2)'''

'''08.Crie um algoritmo que leia notas, definidas pelo usuário, e compute a média delas. 
O código deverá possuir uma função que deve imprimir uma mensagem para o usuário, informando
se ele foi aprovado (se a média for maior ou igual a 70) ou reprovado (caso a média seja menor
que 70).

#Função
def notas (nota1, nota2):

    media = (nota1+nota2)/2

    if media >= 70:
        print('Aprovado')
    else:
        print('Reprovado')

#Programa
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

notas(n1,n2)'''

'''09.Crie uma função que encontre o dobro de um número, caso ele seja positivo ou o triplo
desse número, caso seja negativo. A função deverá imprimir o resultado da execução.'''

#função
def dobroTriplo (n):

    if n > 0:
        print(n*2)
    elif n < 0:
        print(n*3)
    else:
        print('Número Nulo!')

#Programa
n1 = int(input('Digite um número: '))

dobroTriplo(n1)