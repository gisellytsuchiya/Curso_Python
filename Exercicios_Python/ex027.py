#Escreva um programa que leia a velocidade de um carro . se ele ultrapassar
# 80Km/h , mostre uma mensagem dizendo que ele foi multado . A multa vai custar
#R$7,00 por cada Km acima do limite .

print("Olá , serei o seu alarme de velocidade . "
      "\nAcabamos de entrar em uma rodovia , atenção para o limite de velocidade ."
      "\n>>>>80km/h<<<<")
velocidade = float(input("Digite a sua velocidade : "))
multa = (velocidade - 80)* 7.00
if velocidade >80:
    print("VOCÊ ESTÁ SENDO MULTADO , SUA MULTA FICARÁ R${:.2f} .".format(multa))
