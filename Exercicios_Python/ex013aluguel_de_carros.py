# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# calcule o preço a pagar , sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodados.

km = float(input("Digite os Km percorridos no seu trajeto: "))
dias = float(input("Digite a quantidades de dias utilizados :"))
km_soma = (km * 0.15)
dias_soma = (dias * 60)
print("O valor a pagar contando os km percorridos e os dias do carro alugado é R${:.2f}.".format(km_soma+dias_soma))

