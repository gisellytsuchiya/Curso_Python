# Escreva um programa que leia um valor em metros e o exiba
# convertido em centimetros e milímetros .

m = float(input("Digite o valor em metros : "))
c = (m * 100)
mm = (m * 1000)
print("A medida em metros é {:.2f} , em centimetros é {:.2f}, e em milímetros é {:.2f}.".format(m, c, mm))
