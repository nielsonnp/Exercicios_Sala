'''4. Faça um programa que receba dois números inteiros e gere os números inteiros que estão
 no intervalo compreendido por eles.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

for numeros in range (n1,n2,1):
    print(numeros)