#Elabore um programa que calcule o valor a ser pago por um produto , considerando o seu preço normal
# e condição de pagamento : >> a vista dinheiro /cheque : 10% de desconto >> a vista no cartão : 5% de desconto
# >> em até 2x no cartão : preço normal >> 3x ou mais no cartão :25% de juros .

print("Olá , vamos calcular o seu preço final do produto comprado ."
      "\nPOR FAVOR AGUARDE ...")
nome = str(input("Qual o seu nome ? ")).strip().title().split()
print("Muito prazer , {}.".format(nome[0]))
produto = float(input("Me diga o valor do produto ? R$ "))
forma_pagamento = float(input("Me diga qual será a sua forma de pagamento ? "
                            "\npara dinheiro ou cheque : digite 1"
                            "\npara a vista no cartão : digite 2 "
                            "\npara até 2X no cartão : digite 3"
                            "\npara 3X ou mais no cartão : digite 4"
                            "\ndigite :"))
if forma_pagamento == 1:
    dinheiro = produto - ((produto * 10) / 100)
    print("O valor do produto é R${:.2f} , e você ganhou 10% de desconto ."
          "\nO valor a pagar é de R${:.2f}".format(produto, dinheiro))
elif forma_pagamento == 2:
    cartao = produto - ((produto * 5) / 100)
    print("O valor do produto é R${:.2f} , e você ganhou 5% de desconto ."
          "\nO valor a pagar é de R${:.2f} .".format(produto, cartao))
elif forma_pagamento == 3:
    print("O valor do produto é R${:.2f} .".format(produto))
elif forma_pagamento == 4:
    cartao3x = produto +((produto * 25) / 100)
    print("O valor do produto é R${:.2f} , e você pagará 25% de juros ."
          "\nO valor a pagar é de R${:.2f} .".format(produto, cartao3x))