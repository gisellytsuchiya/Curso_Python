#faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade , se
#ele ainda vai se alistar ao serviço militar , se é a hora de se alistar ou se ja passou do tempo
#do alistamento , seu programa tambem devera mostrar o tempo que faltar ou que passou do prazo.

import datetime
print("Seja Bem-Vindo, iremos te ajudar a se informar sobre seu alistamento militar ... ")
nome = str(input("Me diga qual o seu nome ? ")).strip().title().split()
print("Muito Prazer, {}!".format(nome[0]))
idade = str("Informe a sua data de nascimento : ")
print("Sua data de nascimento é {}.".format(idade))


