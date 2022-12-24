# crie um programa que leia o nome de uma cidade e diga
#se ela começa ou não com o nome "santo".

cidade = str(input("Qual o nome da sua cidade :")).strip().lower()
cid = cidade[:6] , "santo" in cidade
print("O nome da sua cidade começa com Santo? {}".format( cid ))
