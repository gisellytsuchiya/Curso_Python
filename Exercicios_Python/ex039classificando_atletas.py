# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de
#um atleta e mostre sua categoria , de acordo com a idade : - até 9 anos : mirim
# - até 14 anos : infantil >>>> - até 19 anos : junior >>>> - até 25 anos : senior >>> - acima : master
import datetime
print("Bem-Vindo ao canal da Confederação Nacional de Natação ."
      "\nVamos começar :")
nome = str(input("Qual o seu nome completo ? ")).strip().title()
pnome = nome.split()
print("Muito prazer em te conhecer, {} !".format(pnome[0]))
ano = datetime.date.today().year
data = int(input("Qual o ano do seu nascimento ? "))
idade = ano - data
print("O Atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Atleta Mirim.")
elif idade <= 14:
    print("Atleta Infantil.")
elif idade <= 19:
    print("Atleta Junior.")
elif idade <= 25:
    print("Atleta Senior.")
elif idade > 25:
    print("Atleta Master.")
