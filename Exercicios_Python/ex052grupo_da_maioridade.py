#Crie um programa que leia o ano de nascimento de sete pessoas . No final , mostre
#quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
atual = datetime.date.today().year
soma = 0
cont = 0
for ano in range (7):
    pessoas = int(input("Digite o ano que você nasceu :"))
    idade = atual - pessoas 
    if idade >= 18:
        soma = soma + 1
    else:
        cont = cont + 1 
print("Apenas {} pessoas atingiram a maior idade.".format(soma))
print("E somente {} pessoas não atingiram a maior idade.".format(cont))