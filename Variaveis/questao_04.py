''' 4. Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

ganho_hora = float(input('Quanto você ganha por hora? '))
hora_mes = float(input('Quantas horas você trabalha no mês? '))

total_salario = (ganho_hora*hora_mes)

print('Seu salário no referido mês é R${:.2f}'.format(total_salario))