#faça um programa que leia o nome completo de uma pessoa .
#mostrando em seguida o primeiro e o ultimo nome separadamente
#ex: ana maria de souza >>> primeiro = ana >>> ultimo = souza.

nome = str(input("Digite seu nome completo : ")).strip().title()
nome = nome.split()
print("Muio prazer em te conhecer ! ")
print("Seu primeiro nome é {} .".format(nome[0]))
print("Seu ultimo nome é {}.".format(nome[len(nome)- 1]))


