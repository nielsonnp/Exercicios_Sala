'''Question 1
Escreva um programa para calcular o fatorial de vários números. Seu programa deve parar
quando ler um número negativo e deve utilizar uma função para realizar o cálculo do
fatorial.'''

def fatorial (n):
    fat = 0
    while (n > 0):
        fat = fat * n
        n = n - 1
    return fat

while True:
    n = int(input("Digite o valor de n: "))
    if n < 0:
        break
print(fatorial(n))