#Faça um programa que leia o sexo de uma pessoa , mas só aceite os valores "m" ou "F". Caso esteja errado , peça a ditação novamente até ter um valor correto . 

sexo = str(input("Informe seu sexo : [ M / F ] ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Dados invalidos . Por favor , informe seu sexo : ")).strip().upper()[0]
print("sexo {} resgistrado com sucesso ".format(sexo))
