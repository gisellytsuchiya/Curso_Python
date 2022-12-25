#Faça um programa que mostre na tela uma contagem regressiva para o estouro de
#fogos de artificios , indo de 10 até 0 , com uma pausa de 1 segundo entre eles .
import time

print("Prontos para a contagem regressiva dos fogos de ano novo ?")
for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)
print("BUM! BUM! POWW!")
