#Refaça o desafio 009 , mostrando a tabuada de um numero que o usuario escolher , só
#que agora utilizando o laço for .


numero = int(input("Digite um numero para ver a tabuada:"))
print("=" * 14)
for tabuada in range(0, 11):
    multiplo = tabuada * numero
    print("{} X {:2} = {}".format(numero, tabuada, multiplo))
print("=" * 14)