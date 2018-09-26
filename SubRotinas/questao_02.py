'''2. Faça um programa, com uma função que receba um valor inteiro. A função retorna
'Valor positivo', se o valor for positivo; 'Valor negativo', se seu argumento for negativo;
ou 'Valor nulo', se o argumento for 0.'''

#função

def negativoPositivo (n1):

    if n1 > 0:
        print('Valor Positivo')
    elif n1 < 0:
        print('Valor Negativo')
    else:
        print('Valor Nulo')
    return n1
 #Programa

n2 = int(input('Digite um Número: '))

print(negativoPositivo(n2))