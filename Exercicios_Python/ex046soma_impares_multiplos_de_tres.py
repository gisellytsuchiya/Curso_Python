#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos
#de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = soma + numero
print(f"A soma de todos {cont} os valores solicitados é {soma}.")
