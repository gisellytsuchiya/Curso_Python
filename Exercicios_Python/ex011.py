#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo
#salário , com 15% de aumento .

salario = float(input("Digite o seu salario :R$"))
soma = (salario * 15)/100
total = (salario + soma)
print("O seu salario ficará {:.2f} com o aumento de 15%.".format(total))
