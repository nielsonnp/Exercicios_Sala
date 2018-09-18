''' 4. Faça um programa que peça a velocidade de um carro para o usuário. Caso ultrapasse
80 km/h, exiba uma mensagem informando que o usuário foi multado. Nesse caso,
imprima o valor da multa, cobrando R$ 5 por km acima de 80km/h.'''

veloc = float(input('Digite a velocidade do carro: '))

multa = (veloc - 80) * 5

if veloc > 80:
    print('Você foi multado em R${} por cada km/h acima de 80km/h \n'
          'cada 1 km acima de 80 km/h é cobrado R$5.00'.format(multa))
else:
    print('Você não foi multado!')