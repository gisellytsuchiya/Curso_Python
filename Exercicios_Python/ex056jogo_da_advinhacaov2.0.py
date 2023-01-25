#Melhore o jogo do desafio 026 , onde o computador vai "pensar" em um numero entre 0 e 10 . Só que agora o jogador vai tentar advinhar até acertar , mostrando no final quantos palpites foram necessarios para vencer. 
import random
print("Vamos jogar um jogo ? ")
jogo = random.randint(0,10)
print("Estou pensando em um número de 0 a 10 . Você terá que advinhar que numero eu pensei .")
acertou = False
palpites = 0
while not acertou :
    escolhido = int(input("Digite o número :"))
    palpites += 1
    if escolhido == jogo:
        acertou = True
    else:
        if escolhido < jogo:
            print("Mais... Tente mais uma vez. ")
        elif escolhido > jogo :
            print("Menos... Tente novamente. ")
print("acertou com {} tentativas , parabens !".format(palpites))

