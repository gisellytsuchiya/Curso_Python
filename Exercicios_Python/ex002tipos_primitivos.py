# Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis
# sobre ele .

frase = str(input("Digite algo : "))
print(type(frase))
print("É um alfa numerico ?",frase.isalpha())
print("É um numero ?", frase.isnumeric())
print("É um alfabeto ?",frase.isalpha())
print("Esta em maiusculo ?",frase.isupper())
print("Esta em minuscula ?",frase.islower())

