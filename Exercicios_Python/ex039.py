# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de
#um atleta e mostre sua categoria , de acordo com a idade : - até 9 anos : mirim
# - até 14 anos : infantil >>>> - até 19 anos : junior >>>> - até 20 anos : senior >>> - acima : master
import datetime
print("Bem-Vindo ao canal da Confederação Nacional de Natação ."
      "\nVamos começar :")
nome = str(input("Qual o seu nome completo ? ")).strip().title()
pnome = nome.split()
print("Muito prazer em te conhecer, {} !".format(pnome[0]))
data = str(input("Qual sua data de nascimento ? "))

if data <= 9:
    print("Atleta Mirim.")
elif data >= 10 and data <= 14:
    print("Atleta Infantil.")
elif data >= 15 and data <= 19:
    print("Atleta Junior.")
elif data == 20:
    print("Atleta Senior.")
elif data > 21:
    print("Atleta Master.")
