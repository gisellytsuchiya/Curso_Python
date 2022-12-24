#Desenvolva um programa que pergunte a distancia de uma viagem em Km . calcule
#o preço da passagem , cobrando R$0,50 por Km para viagens ate 200Km e R$0,45
#para viagens mais longas .

print("Olá , vejo que você quer comprar uma passagem . "
      "\nEu me chamo Diana , e vou te ajudar com isso ."
      "\nPara começarmos preciso de algumas informações .")
nome = str(input("Qual o seu nome completo:")).strip().title()
print("Muito prazer {} .".format(nome))
km = int(input("Qual a quantidade de km tem a sua viagem :"))
if km <= 200:
      print("Sua passagem ficará R${:.2f}.".format(km * 0.50))
else:
      print("Sua passagem ficará R${:.2f}.".format(km * 0.45))
print("Muito obrigada por comprar passagens conosco . ")