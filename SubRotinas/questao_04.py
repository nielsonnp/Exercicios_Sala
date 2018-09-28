'''4. Construa uma função que receba como parâmetros três inteiros: o dia, o mês e o ano.
Sua função deve devolver uma string no formato DD de [mês por extenso] de AAAA.
Valide a data e retorne None caso a data seja inválida.'''

#função
def idade (dia, mes, ano):

    if mes == '1':
        mesDig = 'Janeiro'
    elif mes == '2':
        mesDig = 'Fevereiro'
    elif mes == '3':
        mesDig = 'Março'
    elif mes == '4':
        mesDig = 'Abril'
    elif mes == '5':
        mesDig = 'Maio'
    elif mes == '6':
        mesDig = 'Junho'
    elif mes == '7':
        mesDig = 'Julho'
    elif mes == '8':
        mesDig = 'Agosto'
    elif mes == '9':
        mesDig = 'Setemrbo'
    elif mes == '10':
        mesDig = 'Outubro'
    elif mes == '11':
        mesDig = 'Novembro'
    elif mes == '12':
        mesDig = 'Dezembro'
    else:
        mesDig = 'None'
    return '{} de {} de {}'.format(dia,mesDig,ano)


#programa

dd = int(input('O dia em que você nasceu: '))
mm = str(input('O mês em que você nasceu: '))
aa = int(input('O ano em que você nasceu: '))

print(idade(dd,mm,aa))
