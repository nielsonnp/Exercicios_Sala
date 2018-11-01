'''DESAFIO - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio
de código. Os códigos utilizados são:1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)5 - Voto Nulo/6 - Voto em Branco.
Faça um programa que calcule e mostre:
- O total de votos para cada candidato;
- O total de votos nulos;
- O total de votos em branco;
- A percentagem de votos nulos sobre o total de votos;
- A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''


x = 0
jose = 0
joao = 0
maria = 0
pedro = 0
nulo = 0
branco = 0

while True:

    votos = input('Quem é seu candidato?\n'
                  '1 - José / 2 - João / 3 - Maria / 4 - Pedro / 5 - Nulo / 6 - Branco: ')

    if votos == '0':
        break
    elif votos == '1':
        jose = jose + 1
        print('José')
    elif votos == '2':
        joao = joao + 1
        print('João')
    elif votos == '3':
        maria = maria + 1
        print('Maria')
    elif votos == '4':
        pedro = pedro + 1
        print('Pedro')
    elif votos == '5':
        nulo = nulo + 1
        print('Nulo')
    elif votos == '6':
        branco = branco + 1
        print('Branco')
    else:
        print('Digite um número válido')
    x = x + 1

total = (jose + joao + maria + pedro + nulo + branco)
totalValidos = ((jose + joao + maria + pedro)/total)*100
percNulo = (nulo/total)*100
percBranco = (branco/total)*100

print('\nJosé {} voto(s)\n'
      'João {} voto(s)\n'
      'Maria {} voto(s)\n'
      'Pedro {} voto(s)\n'
      'Nulo {} voto(s)\n'
      'Branco {} voto(s)\n'.format(jose,joao,maria,pedro,nulo,branco))


print('Total de votos: {}'.format(total))
print('Percentagem de votos válidos sobre o total de votos: {:.2f}%'.format(totalValidos))
print('Percentagem de votos nulos sobre o total de votos: {:.2f}%'.format(percNulo))
print('Percentagem de votos em brancos sobre o total de votos: {:.2f}%'.format(percBranco))

