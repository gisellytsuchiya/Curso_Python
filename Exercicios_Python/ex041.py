#Desenvolva uma logica que leia o peso e a altura de uma pessoa ,calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo : >> - abaixo de 18,5 : abaixo do peso >> - entre 18,5 e 25 : peso ideal
#>> - 25 até 30 :sobrepeso >> - 30 ate 40 :  obesidade >> acima de 40 :obesidade morbida.

print("Olá , aqui vamos calcular o seu IMC , em cima da sua altura e peso ...")
print("Vamos lá :")
nome = str(input("Me diga seu nome : ")).strip().title().split()
print("Muito prazer {} ! ".format(nome[0]))
altura = float(input("Qual a sua altura ? "))
peso = float(input("Qual é o seu peso ? "))
imc = peso / altura ** 2
print(">>>CALCULANDO O RESULTADO<<<")
if imc < 18.5:
    print("{} , o seu IMC é de {:.1f} , e você está abaixo do peso.".format(nome[0], imc))
elif imc > 18.5 and imc <= 25:
    print("{} , o seu IMC é de {:.1f} , e você está com o peso ideal.".format(nome[0], imc))
elif imc > 25 and imc <= 30:
    print("{} , o seu IMC é de {:.1f} , e você está com sobrepeso .".format(nome[0], imc))
elif imc > 30 and imc <= 40:
    print("{} , o seu IMC é de {:.1f} , e você está com obesidade .".format(nome[0], imc))
elif imc > 40:
    print("{} , o seu IMC é de {:.1f} , e você está com obesidade morbida .".format(nome[0], imc))