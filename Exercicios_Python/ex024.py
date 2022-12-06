#faça um programa que leia uma frase pelo teclado e mostre :
#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez .
#em que posição ela aparece a última vez .

frase = str(input("Digite uma frase : ")).strip().upper()
print("quantas letras 'A' tem na frase ? {}".format(frase.count("A")))
print("aonde se encontra a primeira letra ? {} ".format(frase.find("A")+1))
print("em que posição ela aparece por ultimo ? {} ".format(frase.rfind("A")+1))