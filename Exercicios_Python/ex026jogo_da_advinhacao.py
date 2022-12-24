#escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
#e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador .
#o programa deverá escrever na tela se o usuario venceu ou perdeu .
import random
print("Oi , para começar me diga : ")
nome = str(input("Qual o seu nome ?")).strip().title()
print("Muito prazer em te conhecer {} .".format(nome))
print("Vamos jogar um jogo ? "
      "Estou pensando em um número de 0 a 5 .")
pergunta = str(input("E você tem que adivinhar qual o número que eu pensei ,okay ?"))
print(pergunta)
if pergunta == "sim":
    print("Então vamos começar ...")
else:
    print("ahh uma pena , quem sabe outra hora!")
jogo = random.randint(0, 5)
print("Pronto , já pensei em um número , agora você terá que tentar descobrir esse número .")
escolhido: int = int(input("Digite o número que você escolheu : "))
if escolhido == jogo:
    print("PARABENS , VOCÊ ACERTOU E GANHOU O JOGO !!")
else:
    print(" {} .... QUE PENA , EU GANHEI , MAIS TENTE DENOVO , VOCÊ CONSEGUE .".format(jogo))