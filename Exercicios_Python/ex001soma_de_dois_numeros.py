# Crie um programa que leia dois números e mostre a soma entre eles .

print("Olá , vamos fazer algumas somas ? ")
n1 = int(input("\033[31mDigite um número : \033[m"))
n2 = int(input("\033[32mDigite outro número : \033[m"))
print("Calculando resultado ... ")
print("A soma entre \033[31m{}\033[m e \033[32m{}\033[m é \033[33m{} \033[m.".format(n1, n2, (n1+n2)))
