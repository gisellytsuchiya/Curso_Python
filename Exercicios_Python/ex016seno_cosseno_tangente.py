# Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno , cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite o valor do angulo :"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno do angulo é {:.2f}."
      "\nO cosseno do angulo é {:.2f}."
      "\nA tangente do angulo é {:.2f}.".format(seno, cosseno, tangente))
