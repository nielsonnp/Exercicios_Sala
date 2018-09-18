''' 5. Ler o preço e a quantidade a ser adquirida de um determinado produto e o valor do desconto,
 em porcentagem. Depois, exibir para o usuário o cálculo do preço total da compra.'''

preco = float(input('Preço do produto: '))
quant = float(input('Quantidade do produto: '))
desconto = float(input('Digite o valor do desconto: '))

total = ((preco*quant) * desconto) / 100

total_desc= (preco*quant - total)

print('Total a pagar com desconto R${:.2f} '. format(total_desc))
