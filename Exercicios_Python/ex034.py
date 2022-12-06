#escreva um programa para aprovar um emprestimo bancario para a compra de uma casa .
# Pergunte o valor da casa , o salario do comprador e em quantos anos ele vai pagar.
# A prestação mensal , não pode exceder 30% do salario ou então o emprestimo será negado .

print("Olá , seja bem vindo ! ")
print("Aqui você pode fazer a simulação do seu emprestimo bancario com mais facilidade e segurança . ")
print("Para começarmos , me diga :")
nome = str(input("Qual o seu nome completo ?")).strip().title().split()
print("Muito prazer em te conhecer, {} .".format(nome[0]))
valor_casa = float(input("Qual o valor da casa que você quer comprar ? R$ "))
salario_cliente = float(input("Agora me diga , qual é o seu salario bruto ? R$ "))
anos = int(input("E em quantos anos pretende pagar , até quitar sua divida ? "))
valor_parcela = valor_casa / (anos * 12)
total_meses = anos * 12
total_salario = salario_cliente - ((salario_cliente * 30) / 100)
if total_salario > valor_parcela:
    print("\033[1;32;40mPARABENS , SEU CREDITO FOI APROVADO COM SUCESSO:\033[m "
          "\nSEGUE ABAIXO AS INFORMAÇÕES DO SEU CADASTRO ."
          "\n{} , o seu salario é de R${:.2f} ,e sua parcela mensal ficou R${:.2f}, foi parcelado em {} meses, total de"
          " {} anos ."
          .format(nome[0], salario_cliente, valor_parcela, total_meses, anos))
else:
    print("\033[1;31;40mSINTO MUITO , MAIS SEU EMPRESTIMO FOI NEGADO . TENTE NOVAMENTE EM ALGUNS MESES .\033[m")