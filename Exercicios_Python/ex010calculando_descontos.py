#faça um algoritmo , que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input("Digite o valor do produto: R$"))
soma = (produto * 5)/100
total = (produto - soma)
print("O produto ficará {:.2f}, com o desconto de 5% .".format(total))