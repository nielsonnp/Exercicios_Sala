'''3. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem;
e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo
para incluir o imposto sobre vendas. Lembrar que o imposto está expresso em porcentagem!!'''

#função

def somaImposto (taxaImposto, custo):

    calculoImposto = (valorCusto * porcenImposto) / 100
    taxaImposto = (valorCusto+calculoImposto)
    return taxaImposto

#programa

valorCusto = float(input('Digite o valor de custo: '))
porcenImposto = float(input('Digite o valor da % do imposto: '))

print('Valor do produto com imposto R${:.2f} '.format(somaImposto(valorCusto,porcenImposto)))


