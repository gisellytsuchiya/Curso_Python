#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la , sabendo
#que cada litro de tinta , pinta uma área de 2m2.

largura = float(input("Digite o tamanho da largura :"))
altura = float(input("Digite o tamanho da altura :"))
area = (largura * altura)
print("Com a largura de {:.2f} , e altura de {:.2f} ,sua area é de {:.2f}. "
      "\nSabendo disso , você precisará de {:.2f} litros para pintar toda a parede. ".format(largura, altura, area, (area/2)))
