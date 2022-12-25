#Crie um programa que mostre na tela todos os numeros pares que estão no intervalo
#entre 1 e 50.
import time

print("Me diga quais os numeros pares entre 1 e 50 ")
for numero in range(0, 51, 2):
    print(numero)
    time.sleep(0.5)
print("Está ai , todos os numeros pares de 1 a 50 ")