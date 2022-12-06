# Faça um programa que leia o comprimento do cateto oposto e
#do cateto adjacente de um triângulo retângulo , calcule  e mostre
#o comprimento da hipotenusa .

co = float(input("Qual o valor do cateto oposto ? "))
ca = float(input("Qual o valor do cateto adjacente ? "))
h = (co / ca)
print("Sabendo que o valor do cateto oposto é {} ,e que o o cateto adjacente é {} , "
      "{:.2f} será o valor da minha hipotenusa."
      .format(co, ca, h))

