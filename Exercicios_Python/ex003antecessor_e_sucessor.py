# Faça um programa que leia um número inteiro e mostre na tela o seu
#sucessor e seu antecessor .

n = int(input("Digite um número : "))
print("O número {}{}{} tem como antecessor {}{}{} e como sucessor {}{}{}.".format("\033[31m", n, "\033[m", "\033[32m",
                                                                                  (n-1), "\033[m", "\033[35m", (n+1), "\033[m"))
