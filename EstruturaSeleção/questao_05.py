''' 5. Tendo como dados de entrada a altura e o sexo de uma pessoa, faça um programa que
calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*altura) - 58
b. Para mulheres: (62.1*altura) - 44.7'''

altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo - F ou M: ')

fem = (62.1*altura) - 44.7
masc = (72.7*altura) - 58

if sexo == 'F':
    print('Seu peso ideal é {}'.format(fem))
elif sexo == 'M':
    print('Seu peso ideal é {}'.format(masc))
else:
    print('Sexo inválido!')
