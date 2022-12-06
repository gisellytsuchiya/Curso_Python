#Escreva um programa que leia dois numeros inteiros e compare-os ,mostrando na tela uma mensagem ;
#- o primeiro valor é maior - o segundo valor é maior - não existe valor maior , os dois são iguais.

numero1 = int(input("Digite um numero inteiro : "))
numero2 = int(input("Digite outro numero inteiro : "))
print("\033[1;35;40m>>>COMPARANDO OS NUMEROS<<< \033[m")
if numero1 > numero2:
    print("o primeiro numero {}, é maior que o numero {}. ".format(numero1, numero2))
elif numero2 > numero1:
    print("O segundo numero {} , é maior que o numero {}.".format(numero2, numero1))
else:
    print("Não existe favor maior , os dois numeros são iguais .")