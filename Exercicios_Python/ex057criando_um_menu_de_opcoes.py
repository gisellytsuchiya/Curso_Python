#crie um programa que leia dois valores e mostre um menu na tela : [1]somar [2]multiplicar [3]maior [4]novos numeros [5]sair do programa . Seu programa deverá realizar a operação solicitada em cada caso .
escolhido = 0
print("Digite dois numero ")
numero1 = int(input("Primeiro numero : "))
numero2 = int(input("Segundo número :"))
while escolhido != 5 :
    print("=" * 20)
    print("[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NUMEROS \n[5]SAIR DO PROGRAMA \n")
    escolhido = int(input(">>>>>>Qual sua opção: "))
    if escolhido == 1:
        soma = numero1 + numero2
        print("A soma do numero {} e do {}, é {}.".format(numero1, numero2, soma))
    elif escolhido == 2:
        multiplicar = numero1 * numero2
        print("O numero {} multiplicado por {} é igual a {}. ".format(numero1, numero2, multiplicar))
    elif escolhido == 3:
        if numero1 > numero2:
            maior = numero1
            print("O maior numero é {}".format(maior))
        elif numero2 > numero1:
            maior = numero2
            print("O maior número é {}.".format(maior))
        else:
            print("Os números são iguais.")
    elif escolhido == 4:
        print("Informe os números novamente :")
        numero1 = int(input("Digite um número : "))
        numero2 = int(input("Digite o segundo número :"))
    elif escolhido == 5:
        print("Aguarde - Finalizando ....")
    else:
        print("Opção invalida , tende novamente !")
print("Fim do programa ! Volte Sempre!")
