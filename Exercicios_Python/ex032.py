#escreva um programa que pergunte o salario de um funcionario e calcule o valor do
# seu aumento .Para salarios superiores a R$1.250,00 , calcule um aumento de 10% ,
#para os inferiores ou iguais , o aumento é de 15%.

print("Bom dia funcionario !"
      "\nvamos ver qual será seu aumento do mês ? ")
salario = float(input("Primeiro me informe o seu atual salario : R$"))
print("calculando resultado ...")
salario10 = (salario * 10 / 100) + salario
salario15 = (salario * 15 / 100) + salario
if salario > 1250.00:
    print("Seu aumento será de 10% , ficará R${:.2f}.".format(salario10))
else:
    print("Seu aumento será de 15% , ficará R${:.2f}.".format(salario15))