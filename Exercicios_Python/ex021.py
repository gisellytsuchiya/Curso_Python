# faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos digitos separados
#ex: digite um numero : 1834
# unidade :4 dezena:3 centena : 8 milhar:1

numero = int(input("Digite um numero de 0 9999:"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando o número {}".format(numero))
print("unidade = {}".format(u))
print("dezena  = {}".format(d))
print("centena = {}".format(c))
print("milhar  = {}".format(m))

