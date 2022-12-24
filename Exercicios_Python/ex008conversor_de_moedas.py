#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar
#Considere US$1.00 = R$3.27

dinheiro = float(input("Quanto você tem na carteira ? R$"))
dolar = (dinheiro / 3.27)
print("Com R${:.2f}, você poderá comprar U${:.2f} de dolar.".format(dinheiro, dolar))
