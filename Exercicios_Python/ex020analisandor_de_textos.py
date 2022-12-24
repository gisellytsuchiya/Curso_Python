# Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras
# maiusculas
# o nome com todas as letras minusculas quantas letras ao todo (sem considerar os espaços)
# quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo :")).strip()
print("nome:{}".format(nome.upper()))
print("nome:{}".format(nome.lower()))
print("O nome completo tem {} letras.".format(len(nome)))
nome = nome.split()
print("E o primeiro nome tem {} letras .".format(len(nome[0])))
