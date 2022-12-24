#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção inteira .
# Ex: Digite um número : 6.127 >>>> O número 6.127 tem a parte Inteira 6
from math import floor
n = float(input("Digite um número qualquer :"))
print("O número {:.2f} tem como parte inteira {} .".format(n, (floor(n))))