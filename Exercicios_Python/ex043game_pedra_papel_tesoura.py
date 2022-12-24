#Crie um programa que faça o computador jogar Jokenpô com você .

import random
print("Olá , vamos jogar um jogo ?"
      "\nVamos começar ...")
print("O jogo é PEDRA , PAPEL E TESOURA :")
regras = int(input("Para saber as regras do jogo basta digitar 0 , caso já conheça as regras digite 1 :"))
if regras == 0:
      print("\033[1;36;40m=-\033[m" * 55)
      print("Eu irei pensar em uma das três possibilidades : PEDRA < PAPEL < TESOURA "
            "\nE você tambem ira pensar em uma delas , no final iremos dizer qual escolhemos e veremos quem ganhou ..."
            "\nPEDRA ganhar de TESOURA e perde para PAPEL >>>>> "
            "\nPAPEL ganhar de PEDRA e perde para TESOURA >>>>> "
            "\nTESOURA ganhar de PAPEL e perde para PEDRA >>>>> ")
      print("\033[1;36;40m=-\033[m" * 55)
else:
      print("\033[1;36;40m=\033[m" * 29)
      print("OK , vamos começar a jogar :")
      print("\033[1;36;40m=\033[m" * 29)
pedra = "PEDRA"
papel = "PAPEL"
tesoura = "TESOURA"
lista = [pedra, papel, tesoura]
escolhido = random.choice(lista)
print("Pense em uma das três possibilidades"
      "\nEu já escolhi , so falta você ...")
adversario = str(input("Digite agora o seu escolhido :")).strip().upper()
print("\033[1;36;40m>>>>>>>>>>JOKENPÔ<<<<<<<<<<\033[m")
if escolhido == adversario:
      print("EMPATE"
            "\nVAMOS JOGAR DE NOVO")
elif escolhido == pedra and adversario == tesoura:
      print("O meu é PEDRA ....."
            "\n\033[1;31;40m<<<<<GANHEI>>>>>\033[m")
elif escolhido == pedra and adversario == papel:
      print("O meu é PEDRA ...."
            "\n\033[1;32;40m<<<<<VOCÊ GANHOU>>>>>\033[m")
elif escolhido == papel and adversario == pedra:
      print("O meu é PAPEL ...."
            "\n\033[1;31;40m<<<<<GANHEI>>>>>\033[m")
elif escolhido == papel and adversario == tesoura:
      print("O meu é PAPEL ...."
            "\n\033[1;32;40m<<<<<VOCÊ GANHOU>>>>>\033[m")
elif escolhido == tesoura and adversario == papel:
      print("O meu é TESOURA ...."
            "\n\033[1;31;40m<<<<<GANHEI>>>>>\033[m")
elif escolhido == tesoura and adversario == pedra:
      print("O meu é TESOURA ...."
            "\n\033[1;32;40m<<<<<VOCÊ GANHOU>>>>>\033[m")