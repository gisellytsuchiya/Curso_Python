#faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade , se
#ele ainda vai se alistar ao serviço militar , se é a hora de se alistar ou se ja passou do tempo
#do alistamento , seu programa tambem devera mostrar o tempo que faltar ou que passou do prazo

import datetime
atual = datetime.date.today().year
print("Seja Bem-Vindo, iremos te ajudar a se informar sobre seu alistamento militar ... ")
nome = str(input("Me diga qual o seu nome ? ")).strip().title().split()
print("Muito Prazer, {}!".format(nome[0]))
print("Vamos começar")
ano = int(input("Informe seu ano de nascimento : "))
idade = atual - ano
print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, atual))
if idade == 18:
    print("Você tem que alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print("Você ainda não tem 18 anos , ainda falta {} anos para se alistar!".format(saldo))
    print("Seu alistamento será em {}.".format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("você já deveria ter se alistado há {} anos .".format(saldo))
    print("Seu alistamento foi em {}.".format(ano))

