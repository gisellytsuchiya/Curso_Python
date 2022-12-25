#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles
#que forem pares . Se o valor digitado for impar , desconsidere-o

cont = 0
soma = 0
for numero in range(6):
    num = int(input("Digite um numero :"))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num

print(f"A soma dos numeros pares é {soma}")
