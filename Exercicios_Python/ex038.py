#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
#no final , de acordo com a media atingida :
#- media abaixo de 5,0 : reprovado - media entre 5,0 e 6,9 : recuperação - media 7,0 ou superior :aprovado

print("Seja Bem-Vindo Professor.")
nota1 = float(input("Digite a primeira nota do aluno : "))
nota2 = float(input("Digite a segunda nota do aluno : "))
nota_final = (nota1 + nota2) / 2
print(">>>>CALCULANDO RESULTADO , AGUARDE .....<<<<")
if nota_final < 5.0:
    print("\033[1;31;40mREPROVADO\033[m"
          "\nSua nota final foi {:.1f} .".format(nota_final))
elif nota_final >= 5.0 and nota_final <= 6.9:
    print("\033[1;33;40mRECUPERAÇÃO\033[m"
          "\nSua nota final foi {:.1f} .".format(nota_final))
else:
    print("\033[1;32;40mAPROVADO\033[m"
          "\nSua nota final foi {:.1f} .".format(nota_final))